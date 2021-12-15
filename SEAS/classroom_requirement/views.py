from django.shortcuts import render

# Create your views here.
from django.db import connection
# from .forms import SessionSelectorForm

"""  
--------------------------------------------------------------------------------
For Classroom Requirements page
--------------------------------------------------------------------------------
"""

def index(request):
    """  
    --------------------------------------------------
    Getting List of Years and Semesters from Database
    --------------------------------------------------
    """
    query = """     
            SELECT dYear
            FROM Section_T
            GROUP BY dYear
            ORDER BY dYear
            """
    years = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        years = cursor.fetchall()

    query = """     
            SELECT eSession
            FROM Section_T
            GROUP BY eSession
            """
    sessions = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        sessions = cursor.fetchall()

    """  
    --------------------------------------------------
    Checking to see if form in template returns value 
    or else returns default value
    --------------------------------------------------
    """
    tableHeaders = []
    tableData = []

    year = ''
    session = ''


    if request.method == 'POST':
        year = request.POST.get('selectedYear', 2021)
        session = request.POST.get('selectedSession', "Summer")

    else:
        year = years[-1][0]
        session = sessions[-1][0]

    """  
    --------------------------------------------------
    Query that groups by enrollment ranges and does the
    arithmetic needed to get required rooms for different
    slots based on year and session selection. Any value
    that does not fall in the range is shown separately.
    --------------------------------------------------
    """

    query = """
            SELECT X.Class_Size AS "Class Size", X.Sections, X.Class_Room_6 AS "Class Room 6", X.Class_Room_7 AS "Class Room 7"
            FROM(
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
                        ELSE '0'
                    END 
                ) AS Class_Size, COUNT(*) AS Sections, ROUND(COUNT(*)/12, 1) AS Class_Room_6, ROUND(COUNT(*)/14, 1) AS Class_Room_7
                FROM Section_T S
                WHERE 
                        dYear = %(year)s 
                    AND eSession = %(session)s
                GROUP BY Class_Size
                HAVING Class_Size != '0'
                ORDER BY Class_Size ASC
            ) X

            UNION

            SELECT *
            FROM(
                SELECT ( 
                    CASE 
                        WHEN S.nEnrolled > 65 THEN S.nEnrolled
                        ELSE 0
                    END 
                ) AS Class_Size, COUNT(*) AS Sections, ROUND(COUNT(*)/12, 1) AS Class_Room_6, ROUND(COUNT(*)/14, 1) AS Class_Room_7
                FROM Section_T S
                WHERE 
                        dYear = %(year)s 
                    AND eSession = %(session)s
                GROUP BY Class_Size
                HAVING Class_Size != 0
                ORDER BY Class_Size ASC
            ) Y

            UNION
            
            SELECT ( 
                CASE 
                    WHEN S.nEnrolled > 0 THEN 'Total'
                    ELSE '0'
                END 
            ) AS Class_Size, COUNT(*), ROUND(COUNT(*)/12, 1), ROUND(COUNT(*)/14, 1)
            FROM Section_T S
            WHERE 
                    dYear= %(year)s 
                AND eSession = %(session)s
            GROUP BY Class_Size
            HAVING Class_Size != '0'
            
            """
    values={
        "year" : str(year),
        "session" : session,
    }
    with connection.cursor() as cursor:
        cursor.execute( query , values)
        # print(connection.queries)
        tableHeaders = [ col[0] for col in cursor.description ]
        tableData = cursor.fetchall()   


    context = {
        'tableHeaders': tableHeaders,
        'tableData'   : tableData,
        'years'       : years,
        'sessions'    : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
    }

    return render(request, 'classroom_requirement/tablechart.html', context)

