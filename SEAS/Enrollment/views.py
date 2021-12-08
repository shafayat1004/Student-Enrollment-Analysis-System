from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Suhaila's stuff
# path( 'Enrollment/', include('Enrollment.urls') ),


# Create your views here.
def schoolWiseEnroll( request ):
    ''' School wise enrollment Table [Compact]'''
    # Fetch all schools and create select clause for them
    query = """
        SELECT cSchool_ID AS sch
	    FROM School_T;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        schools = [ row[0] for row in cursor.fetchall() ]

        sqlClause = ""
        for school in schools:
            sqlClause += f"SUM( CASE WHEN E.School = '{school}' THEN Counter ELSE 0 END ) AS {school},\n"

    # Run query for revenue data of all schools
    query = f"""
        SELECT 
		    Enrollment ,
            {sqlClause}
            SUM( Counter ) AS Total
        FROM (
		SELECT 
			nEnrolled AS Enrollment, 
			COUNT(nEnrolled) AS Counter , 
			D.cSchool_ID AS School
		FROM Section_T AS S, CoOfferedCourse_T O, Course_T C, Department_T D
		WHERE 
				S.cCoffCode_ID = O.cCoffCode_ID
			AND O.cCourse_ID = C.cCourse_ID 
			AND C.cDepartment_ID = D.cDepartment_ID 
			AND dYear= '2021'					 	-- replace with {{django}}
			AND eSession = 'Spring'					-- replace with {{django}}
			GROUP BY Enrollment, School
			ORDER BY D.cSchool_ID, Enrollment ASC
        
    ) E 
    GROUP BY Enrollment
    ORDER BY Enrollment ASC
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    return HttpResponse( labels )       # for debug only
    '''
    return render( request, "revenue.html", { 
            'labels': labels,
            'data': data,
        }
    )
    '''


