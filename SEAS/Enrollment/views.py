from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .utils import schoolEnrollChartDataPacker
# Suhaila's stuff



# Create your views here.
def schoolWiseEnrollExpand( request ):
    ''' School wise enrollment Table [Expanded]'''

    tableCol = []
    tableRow = []
    '''' Store all years '''
    query = """     
            SELECT dYear
            FROM Section_T
            GROUP BY dYear
            """
    years = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        years = cursor.fetchall()

    '''' Store all sessions '''
    query = """     
            SELECT eSession
            FROM Section_T
            GROUP BY eSession
            """
    sessions = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        sessions = cursor.fetchall()

    # Fetch all schools and create select clause for them
    query = """
        SELECT cSchool_ID AS sch
	    FROM School_T;
    """
    with connection.cursor() as cursor:
        cursor.execute( query )
        schools = [ row[0] for row in cursor.fetchall() ]  
    
    year = ''
    session = ''
    
    if request.method == 'POST':
        year = request.POST.get('selectedYear', 2021)
        session = request.POST.get('selectedSession', "Summer")

    else:
        year = years[-1][0]
        session = sessions[-1][0]

    '''
    SCHOOL WISE ENROLLMENT TABLE [Expanded]
    ---------------------------------------------------------------------------------------------------------------
    This query creates a view which contains which joins the section, course and school table together in a single
    table.
    ---------------------------------------------------------------------------------------------------------------
    '''
    #create section view 
    query = '''
        CREATE VIEW sections_v AS
    SELECT *, ( T.Enrolled * T.Credits ) AS TotalCredits
    FROM (
        SELECT 
            CONCAT( C.cCourse_ID, '-', S.nSectionNumber ) AS Section, 
            S.dYear AS Years, 
            S.eSession AS Sessions,
            S.nEnrolled AS Enrolled,
            C.nCreditHours AS Credits,
            D.cDepartment_ID AS Department,
            D.cSchool_ID AS School
        FROM 
            Section_T S, CoOfferedCourse_T O, Course_T C, Department_T D
        WHERE 
                S.cCoffCode_ID = O.cCoffCode_ID
            AND O.cCourse_ID = C.cCourse_ID 
           AND S.cDepartment_ID = D.cDepartment_ID
		
        ORDER BY Years, Sessions DESC, Section, Credits, Department, School
    ) T;
     
    '''
    try :
        with connection.cursor() as cursor:
            cursor.execute( query )
    except:
        pass
      #  section = cursor.fetchall() 

    ''''
    SCHOOL WISE ENROLLMENT TABLE [Expanded]
    --------------------------------------------------
     This is the query for getting numbers of courses 
     being offered in each school with respect
     to the Enrollment which gets incremented by one.
    --------------------------------------------------
    '''

    sqlClause = ""
    for school in schools:
        sqlClause += f"SUM( CASE WHEN E.School = '{school}' THEN Counter ELSE 0 END ) AS {school},\n"
     
    query = f"""
        SELECT 
		    Enrollment ,
            {sqlClause}
            SUM( Counter ) AS Total
        FROM (
            SELECT 
                nEnrolled AS Enrollment, 
                COUNT(nEnrolled) AS Counter, 
                D.cSchool_ID AS School
            FROM Section_T AS S, Department_T D
            WHERE 
                    S.cDepartment_ID = D.cDepartment_ID 
                AND dYear= '{year}'					 
                AND eSession = '{session}'					
                GROUP BY Enrollment, School
                ORDER BY D.cSchool_ID, Enrollment ASC    
        ) E 
        WHERE Enrollment > 0
        GROUP BY Enrollment
        UNION
        SELECT 
            9999,                   -- this should be "Total" but as we were facing issues with ordering we places this number. 
            {sqlClause}
            SUM( Counter) AS T  
        FROM (
            SELECT 
                School,
                COUNT(Enrolled) AS Counter  
            FROM sections_v 
            WHERE  
                    Years = '{year}' 
                AND Sessions = '{session}' 
                AND Enrolled != 0
            GROUP BY School
        ) E
        ORDER BY Enrollment ASC;
    """

    values={
        "year" : str(year),
        "session" : session,
    }
    with connection.cursor() as cursor:
        cursor.execute( query,values )
        tableCol = [ col[0] for col in cursor.description ]
        tableRow = cursor.fetchall()
    
    context = {
        'tableCol': tableCol,
        'tableRow'  : tableRow,
        'years'       : years,
        'sessions'    : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
    }
    return render(request, 'Enrollment/School-Wise-Enroll-Expand.html', context)
    

def schoolWiseEnrollCompact( request ):
    ''' School wise enrollment Table [Compact]'''

    '''' Store all years '''
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

    '''' Store all sessions '''
    query = """     
            SELECT eSession
            FROM Section_T
            GROUP BY eSession
            """
    sessions = []
    with connection.cursor() as cursor:
        cursor.execute(query)
        sessions = cursor.fetchall()

    # Fetch all schools and create select clause for them
    query = """
        SELECT cSchool_ID AS sch
	    FROM School_T;
    """
    
    with connection.cursor() as cursor:
        cursor.execute( query )
        schools = [ row[0] for row in cursor.fetchall() ]

    year = ''
    session = ''
    
    if request.method == 'POST':
        year = request.POST.get('selectedYear', 2021)
        session = request.POST.get('selectedSession', "Summer")

    else:
        year = years[0][0]
        session = sessions[0][0]

    '''
    SCHOOL WISE ENROLLMENT TABLE [COMPACT]
    --------------------------------------------------
    This query generates school wise number of sections 
    being offered with respect to the class sizes as well 
    as total sections for all schools.
    --------------------------------------------------
    '''
    
    sqlClause = ""
    for school in schools:
        sqlClause += f"SUM( CASE WHEN E.School = '{school}' THEN Counter ELSE 0 END ) AS {school},\n"

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
		FROM Section_T S, Department_T D
		WHERE 
				S.cDepartment_ID = D.cDepartment_ID 
			AND dYear= '{year}'					 
			AND eSession = '{session}'				 
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

    values={
        "year" : str(year),
        "session" : session,
    }
    xAxis, yAxis, totals = schoolEnrollChartDataPacker( data, labels )
    
    context = {
        'labels': labels,
        'data'  : data,
        'years'       : years,
        'sessions'    : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
        #'xAxis' : xAxis,
        #'yAxis': yAxis ,
       # 'totals' : totals,
    }
    return render(request, 'Enrollment/School-Wise-Enroll-Compact.html', context)
    
#'Enrollment/School-Wise-Enroll-Compact.html'

