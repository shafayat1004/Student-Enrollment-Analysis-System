from django.shortcuts import render

from django.db import connection

def resourceUsage(request):
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

        
    tableHeaders = []
    tableData = []

    year = ''
    session = ''


    if request.method == 'POST':
        year = request.POST.get('selectedYear', 2021)
        session = request.POST.get('selectedSession', "Summer")

    else:
        year = years[0][0]
        session = sessions[0][0]

    query = """
            SELECT
                School AS '', 
                Sum,
                ROUND( AvgEnroll , 2) AS AvgEnroll,
                ROUND( AvgRoom, 2 ) AS AvgRoom,
                ROUND( Difference, 2 ) AS Difference,
                ROUND( ( (Difference / AvgRoom)*100 ), 2 ) AS 'Unused%%'
            FROM (
                SELECT 
                    D.cSchool_id AS School,
                    SUM( S.nEnrolled ) AS Sum,
                    AVG( S.nEnrolled ) AS AvgEnroll, 
                    AVG( Cr.nRoomCapacity ) AS AvgRoom,
                    ( AVG( Cr.nRoomCapacity ) - AVG( S.nEnrolled ) ) AS Difference
                    
                FROM
                    Department_T AS D
                    INNER JOIN Course_T AS C            ON D.cDepartment_ID = C.cDepartment_ID
                    INNER JOIN CoOfferedCourse_T AS Co  ON C.cCourse_ID = Co.cCourse_ID
                    INNER JOIN Section_T AS S           ON Co.cCoffCode_ID = S.cCoffCode_ID
                    INNER JOIN Classroom_T AS Cr        ON S.cRoom_ID = Cr.cRoom_ID
                WHERE
                        S.eSession = %(session)s
                    AND S.dYear = %(year)s 
                GROUP BY D.cSchool_id
            ) T
            UNION
            SELECT 
                S.eSession AS Session,
                SUM( S.nEnrolled ) AS Sum,
                ROUND( AVG( S.nEnrolled ), 2) AS AvgEnroll, 
                ROUND( AVG( Cr.nRoomCapacity ), 2) AS AvgRoom,
                ROUND( ( AVG( Cr.nRoomCapacity ) - AVG( S.nEnrolled ) ), 2) AS Difference,
                -- ROUND( ( (Difference / AvgRoom)*100 ), 2 )
                ROUND( ( (( AVG( Cr.nRoomCapacity ) - AVG( S.nEnrolled ) ) / (ROUND( AVG( Cr.nRoomCapacity ), 2)))*100 ), 2 )
                
            FROM
                Department_T AS D
                INNER JOIN Course_T AS C            ON D.cDepartment_ID = C.cDepartment_ID
                INNER JOIN CoOfferedCourse_T AS Co  ON C.cCourse_ID = Co.cCourse_ID
                INNER JOIN Section_T AS S           ON Co.cCoffCode_ID = S.cCoffCode_ID
                INNER JOIN Classroom_T AS Cr        ON S.cRoom_ID = Cr.cRoom_ID
            WHERE
                    S.eSession = %(session)s
                AND S.dYear = %(year)s
            GROUP BY Session;
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

    return render(request, 'resources/resource_usage.html', context)

def iubResources(request):

    return render(request, 'resources/iub_resources.html')
def resourceComp(request):
    return render(request, 'resources/resource_comparison.html')