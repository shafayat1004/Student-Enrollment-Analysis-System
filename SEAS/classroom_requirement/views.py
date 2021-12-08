from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db import connection

def index(request):

    labels = []
    data = []

    query = """
            SELECT ( 
                CASE 
                    WHEN S.nEnrolled BETWEEN  1 AND 10 THEN '1-10'  
                    WHEN S.nEnrolled BETWEEN 11 AND 20 THEN '11-20'  
                    WHEN S.nEnrolled BETWEEN 21 AND 30 THEN '21-30'  
                    WHEN S.nEnrolled BETWEEN 31 AND 35 THEN '31-35'  
                    WHEN S.nEnrolled BETWEEN 36 AND 40 THEN '36-40'  
                    WHEN S.nEnrolled BETWEEN 41 AND 50 THEN '41-50'  
                    WHEN S.nEnrolled BETWEEN 51 AND 55 THEN '51-55' 
                    WHEN S.nEnrolled BETWEEN 56 AND 65 THEN '56-65' 
                    WHEN S.nEnrolled > 65 THEN '65+'
                    ELSE '0'
                END 
            ) AS Class_Size, COUNT(*) AS Sections, ROUND(COUNT(*)/12, 1) AS Class_Room_6, ROUND(COUNT(*)/14, 1) AS Class_Room_7
            FROM Section_T S, CoOfferedCourse_T O, Course_T C, Department_T D
            WHERE 
                    S.cCoffCode_ID = O.cCoffCode_ID
                AND O.cCourse_ID = C.cCourse_ID 
                AND C.cDepartment_ID = D.cDepartment_ID 
                AND dYear= "2021" 
                AND eSession = "Spring"
            GROUP BY Class_Size
            HAVING Class_Size != '0'

            UNION

            SELECT ( 
                CASE 
                    WHEN S.nEnrolled > 0 THEN 'Total'
                    ELSE '0'
                END 
            ) AS Class_Size, COUNT(*), ROUND(COUNT(*)/12, 1), ROUND(COUNT(*)/14, 1)
            FROM Section_T S, CoOfferedCourse_T O, Course_T C, Department_T D
            WHERE 
                    S.cCoffCode_ID = O.cCoffCode_ID
                AND O.cCourse_ID = C.cCourse_ID 
                AND C.cDepartment_ID = D.cDepartment_ID 
                AND dYear= "2021" 
                AND eSession = "Spring"
            GROUP BY Class_Size
            HAVING Class_Size != '0'
            ORDER BY Class_Size ASC;
            """

    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()
        

    context = {
        'labels': labels,
        'data'  : data,
    }

    return render(request, 'classroom_requirement/tablechart.html', context)

