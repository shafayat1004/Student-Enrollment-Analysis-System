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
                    INNER JOIN Section_T AS S           ON D.cDepartment_ID = S.cDepartment_ID
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
                INNER JOIN Section_T AS S           ON D.cDepartment_ID = S.cDepartment_ID
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

    tableHeaders2 = []
    tableData2 = []

    query = """
        SELECT 
            C.nRoomCapacity AS "Class Size", 
            COUNT(DISTINCT S.cRoom_ID) AS "IUB Resources",
            (COUNT(DISTINCT S.cRoom_ID) * C.nRoomCapacity) AS "Capacity"
        FROM Classroom_T C, Section_T S
        WHERE C.cRoom_ID=S.cRoom_ID AND S.dYear >= 2019
        GROUP BY C.nRoomCapacity

        UNION

        SELECT "Total", SUM(X.resources), SUM(X.capacity)
        FROM (
            SELECT 
                C.nRoomCapacity AS "Class Size", 
                COUNT(DISTINCT S.cRoom_ID) AS resources,
                (COUNT(DISTINCT S.cRoom_ID) * C.nRoomCapacity) AS capacity
            FROM Classroom_T C, Section_T S
            WHERE C.cRoom_ID=S.cRoom_ID AND S.dYear >= 2019
            GROUP BY C.nRoomCapacity
        ) AS X;
        """
    
    with connection.cursor() as cursor:
        cursor.execute( query)
        # print(connection.queries)
        tableHeaders2 = [ col[0] for col in cursor.description ]
        tableData2 = cursor.fetchall()

    totCap6  = float(tableData2[-1][-1] * 12)
    totCap7 = float(tableData2[-1][-1] * 14)
    avg6 = round(totCap6/3.5)
    avg7 = round(totCap7/3.5)
    free6 = round(avg6 * (100 - tableData[-1][-1])/100)
    free7 = round(avg7 * (100 - tableData[-1][-1])/100)
    
    context = {
        'tableHeaders': tableHeaders,
        'tableData'   : tableData,
        'tableHeaders2': tableHeaders2,
        'tableData2'   : tableData2,
        'years'       : years,
        'sessions'    : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
        'totCap6'     : round(totCap6),
        'totCap7'     : round(totCap7),
        'avg6'        : avg6,
        'avg7'        : avg7,
        'free6'       : free6,
        'free7'       : free7,
    }

    return render(request, 'resources/resource_usage.html', context)


def resourceComp(request):
   
    return render(request, 'resources/resource_comparison.html')