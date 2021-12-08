from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Suhaila's stuff
# path( 'Enrollment/', include('Enrollment.urls') ),


# Create your views here.
def schoolWiseEnrollExpand( request ):
    ''' School wise enrollment Table [Expanded]'''
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

    # Run query for School wise enrollment data
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
    WHERE Enrollment != 0
    GROUP BY Enrollment
    ORDER BY Enrollment ASC;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    # return HttpResponse( labels )       # for debug only
    
    context = {
        'labels': labels,
        'data'  : data,
    }
    return render(request, 'Enrollment/School-Wise-Enroll-Expand.html', context)
    

def schoolWiseEnrollCompact( request ):
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

    # Run query for school wise enrollment data
    query = f"""
        SELECT 
		    Enrollment ,
            {sqlClause}
            SUM( Counter ) AS Total
        FROM (
		SELECT ( 
			CASE 
				-- WHEN S.nEnrolled < 1 THEN '  0'
				WHEN S.nEnrolled BETWEEN  1 AND 10 THEN '  1-10'  
				WHEN S.nEnrolled BETWEEN 11 AND 20 THEN ' 11-20'  
				WHEN S.nEnrolled BETWEEN 21 AND 30 THEN ' 21-30'  
				WHEN S.nEnrolled BETWEEN 31 AND 35 THEN ' 31-35'  
				WHEN S.nEnrolled BETWEEN 36 AND 40 THEN ' 36-40'  
				WHEN S.nEnrolled BETWEEN 41 AND 50 THEN ' 41-50'  
				WHEN S.nEnrolled BETWEEN 51 AND 55 THEN ' 51-55' 
				WHEN S.nEnrolled BETWEEN 56 AND 60 THEN ' 56-60' 
				WHEN S.nEnrolled > 60 THEN ' 60+'
			END 
		) AS Enrollment, D.cSchool_ID AS School, COUNT(*) AS Counter
		FROM Section_T S, CoOfferedCourse_T O, Course_T C, Department_T D
		WHERE 
				S.cCoffCode_ID = O.cCoffCode_ID
			AND O.cCourse_ID = C.cCourse_ID 
			AND C.cDepartment_ID = D.cDepartment_ID 
			AND dYear= '2021'					 -- replace with {{django}}
			AND eSession = 'Spring'				 -- replace ''     ''
		GROUP BY Enrollment, School
		ORDER BY School, Enrollment ASC
    ) E
    WHERE Enrollment != 0
    GROUP BY Enrollment
	ORDER BY Enrollment;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    # return HttpResponse( labels )       # for debug only
    context = {
        'labels': labels,
        'data'  : data,
    }
    return render(request, 'Enrollment/School-Wise-Enroll-Compact.html', context)
    


