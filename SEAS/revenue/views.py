from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

from .utils import iubRevenueChartDataPacker, deptRevenueChartDataPacker

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


    """
    REVENUE OF IUB
    --------------------------------------------------------
    Query that sums up the revenue of all sections by school
    and groups them by semester and year. Percentage change 
    in revenue is calculated by using the current semester 
    revenue total and the revenue total of the same semester 
    session of the previous year.
    --------------------------------------------------------
    """
    query = f"""
        SELECT 
            CONCAT( Years, ' ',  Sessions ) AS 'Semester',
            {sqlClause}
            SUM( Revenue ) AS Total,
            ROUND( 
                100 * ( 
                    SUM( Revenue ) - LAG( SUM( Revenue ), 3,  SUM( Revenue ) ) OVER () 
                ) / SUM( Revenue ) 
            ) AS '% Change'
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
                ) M
            WHERE 
                    S.cCoffCode_ID = O.cCoffCode_ID
                AND O.cCourse_ID = C.cCourse_ID 
                AND S.cDepartment_ID = D.cDepartment_ID
                AND S.dYear = M.Years
                AND S.eSession = M.Sessions
            GROUP BY Years, Sessions, School
            ORDER BY Years, Sessions
        ) E
        GROUP BY Years, Sessions
        ORDER BY Years, Sessions DESC
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    xAxis, yAxis, totals, changes = iubRevenueChartDataPacker( data, labels )

    return render( request, "revenue/revenue_iub.html", { 
            'colNames': labels,
            'revenues': data,
            'xAxis': xAxis,
            'yAxis': yAxis ,
            'totals': totals,
            'changes': changes 
        }
    )


def deptRevenue( request ):
    ''' Historical revenue data and change of all the departments in a school'''
    # Fetch all schools for form
    query = """
        SELECT cSchool_ID AS sch
	    FROM School_T;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        schools = [ row[0] for row in cursor.fetchall() ]

    if request.method == 'POST':
        schoolSelected = request.POST.get("selectedSchool")
    else:
        return render( request, "revenue/revenue_dept.html", { 'schools': schools, } )

    # Fetch departments of the selected school and create select clause for them
    query = f"""
        SELECT cDepartment_ID AS dep
        FROM Department_T
        WHERE cSchool_ID = '{schoolSelected}'			-- replace with django
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        departments = [ row[0] for row in cursor.fetchall() ]

    depNames = ""
    depColSqlClause = ""
    depPercentColSqlClause = ""
    for dept in departments:
        depNames += f"{dept}, "
        depColSqlClause += f"SUM( CASE WHEN Department = '{dept}' THEN Revenue ELSE 0 END ) AS {dept},\n"
        depPercentColSqlClause += f"ROUND( 100 * ( SUM( {dept} ) - LAG( SUM( {dept} ), 3,  SUM( {dept} ) ) OVER () ) / SUM( {dept} ) ) AS '%{dept}',\n"
  
    """  
    REVENUE OF THE SELECTED SCHOOL
    --------------------------------------------------------
    Query that sums up the revenue of each section of the
    selected school by department and groups them by semester 
    and year. Percentage change in revenue is calculated by 
    using the current semester revenue and the revenue
    of the same semester session of the previous year.
    --------------------------------------------------------
    """
    query = f"""
        SELECT 
            CONCAT( Years, ' ',  Sessions ) AS 'Semester',
            {depNames}
            {schoolSelected},
            {depPercentColSqlClause}
            ROUND( 
                100 * (
                    {schoolSelected} - ( LAG( {schoolSelected}, 3,  {schoolSelected} )  OVER () ) 
                ) / SUM( {schoolSelected} ) 
            ) AS '%{schoolSelected}'
        FROM (
            SELECT 
                Years,
                Sessions, 
                {depColSqlClause}
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
                    ) M
                WHERE 
                        S.cCoffCode_ID = O.cCoffCode_ID
                    AND O.cCourse_ID = C.cCourse_ID 
                    AND S.cDepartment_ID = D.cDepartment_ID
                    AND D.cSchool_ID = '{schoolSelected}'
                    AND S.dYear = M.Years
                    AND S.eSession = M.Sessions
                GROUP BY Years, Sessions, Department
            ) E
            GROUP BY Years, Sessions
            ORDER BY Years, Sessions
        ) K
        GROUP BY Years, Sessions
        ORDER BY Years, Sessions DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()

    xAxis, yAxis = deptRevenueChartDataPacker( data, labels )
        
    return render( request, "revenue/revenue_dept.html", { 
            'colNames': labels,
            'revenues': data,
            'xAxis': xAxis,
            'yAxis': yAxis,
            'schoolSelected': schoolSelected,
            'schools': schools,
        }
    )