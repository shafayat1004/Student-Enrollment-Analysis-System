from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Fahim's stuff
# path( 'revenue/', include('revenue.urls') ),


# Create your views here.
def revenueMain( request ):
    return HttpResponse("Hallo we like monay over here")


def iubRevenue( request ):
    ''' Historical revenue data and change of all the schools in IUB'''
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
            sqlClause += f"SUM( CASE WHEN E.School = '{school}' THEN Revenue ELSE 0 END ) AS {school},\n"

    # Run query for revenue data of all schools
    query = f"""
        SELECT 
            CONCAT( Years, ' ',  Sessions ) AS 'Semester',
            {sqlClause}
            SUM( Revenue ) AS Total
        FROM (
            SELECT 
                Years, 
                Sessions, 
                SUM( S.nEnrolled * C.nCreditHours ) AS Revenue, 
                D.cSchool_ID AS School
            FROM 
                Section_T S, 
                CoOfferedCourse_T O, 
                Course_T C,
                Department_T D, 
                (	
                    SELECT dYear AS Years, eSession AS Sessions
                    FROM Section_T
                    GROUP BY dYear, eSession
                    ORDER BY dYear, eSession
                ) M
            WHERE 
                    S.cCoffCode_ID = O.cCoffCode_ID
                AND O.cCourse_ID = C.cCourse_ID 
                AND C.cDepartment_ID = D.cDepartment_ID
                AND S.dYear = M.Years
                AND S.eSession = M.Sessions
            GROUP BY Years, Sessions, School
            ORDER BY Years, Sessions DESC
        ) E
        GROUP BY Years, Sessions
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()
        
    return render( request, "revenue_iub.html", { 
            'colNames': labels,
            'revenues': data,
        }
    )


def deptRevenue( request ):
    ''' Historical revenue data and change of all the departments in the selected school'''
    # Fetch departments of the selected school and create select clause for them
    schoolSelected = "SETS"     # fetch from form

    query = f"""
        SELECT cDepartment_ID AS dep
        FROM Department_T
        WHERE cSchool_ID = '{schoolSelected}'			-- replace with django
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        departments = [ row[0] for row in cursor.fetchall() ]

        sqlClause = ""
        for dept in departments:
            sqlClause += f"SUM( CASE WHEN Department = '{dept}' THEN Revenue ELSE 0 END ) AS {dept},\n"
  
    # Run query for revenue data for the departments
    query = f"""
        SELECT 
            CONCAT( Years, ' ',  Sessions ) AS 'Semester',
            {sqlClause}
            SUM( Revenue ) AS {schoolSelected}
        FROM (
            SELECT 
                Years, 
                Sessions, 
                SUM( S.nEnrolled * C.nCreditHours ) AS Revenue, 
                D.cDepartment_ID AS Department
            FROM 
                Section_T S, 
                CoOfferedCourse_T O, 
                Course_T C,
                Department_T D, 
                (	
                    SELECT dYear AS Years, eSession AS Sessions
                    FROM Section_T
                    GROUP BY dYear, eSession
                    ORDER BY dYear, eSession
                ) M
            WHERE 
                    S.cCoffCode_ID = O.cCoffCode_ID
                AND O.cCourse_ID = C.cCourse_ID 
                AND C.cDepartment_ID = D.cDepartment_ID
                AND D.cSchool_ID = '{schoolSelected}'
                AND S.dYear = M.Years
                AND S.eSession = M.Sessions
            GROUP BY Years, Sessions, Department
            ORDER BY Years, Sessions DESC
        ) E
        GROUP BY Years, Sessions;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    return render( request, "revenue_dept.html", { 
            'colNames': labels,
            'revenues': data,
        }
    )