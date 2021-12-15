from django.shortcuts import render

from django.db import connection

"""  
--------------------------------------------------------------------------------
For USAGE OF THE RESUORCES page
--------------------------------------------------------------------------------
"""

def resourceUsage(request):
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
    Run query based on selected year and session value
    for USAGE OF RESOURCE TABLE
    --------------------------------------------------
    """

    usageOfResourcesQuery = """
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
        cursor.execute( usageOfResourcesQuery , values)
        # print(connection.queries)
        tableHeaders = [ col[0] for col in cursor.description ]
        tableData = cursor.fetchall()   

    """  
    --------------------------------------------------
    Run a useless query based on hardcoded values
    for IUB AVAILABLE RESOURCES TABLE
    (scope for future custom room count form selection)
    --------------------------------------------------
    """

    tableHeaders2 = []
    tableData2 = []

    rooms = [(20, 20), (30, 3), (35, 18), (40, 10), (50, 34), (54, 1), (64, 2), (124, 3), (168, 1)]

    roomGenerationQuery = ''
    ranNever = True
    for i, room in enumerate(rooms):
        if ranNever:
            roomGenerationQuery = "SELECT " + str(room[0]) + " AS Class_Size, " + str(room[1]) + " AS nRooms UNION"
            ranNever = False
        if i == len(rooms)-1:
            roomGenerationQuery += "\nSELECT " + str(room[0]) + " , " + str(room[1])    
            break
        roomGenerationQuery += "\nSELECT " + str(room[0]) + " , " + str(room[1]) + " UNION"

    query = f"""
            SELECT Class_Size AS "Class Size", nRooms AS "IUB Resource", (Class_Size*nRooms) AS "Capacity"
            FROM(
                {roomGenerationQuery}
            ) AS iubResource
                
            UNION

            SELECT "Total", SUM(nRooms) , SUM(Class_Size*nRooms)
            FROM(
                {roomGenerationQuery}
            ) AS iubResource
            """
    
    with connection.cursor() as cursor:
        cursor.execute( query )
        # print(connection.queries)
        tableHeaders2 = [ col[0] for col in cursor.description ]
        tableData2 = cursor.fetchall()


    """  
    --------------------------------------------------
    Calculations for lower half of
    IUB AVAILABLE RESOURCES TABLE
    Taking into account that user might load a 
    semester that doesn't exist in database
    --------------------------------------------------
    """

    try:
        totCap6  = float(tableData2[-1][-1] * 12)
        totCap7 = float(tableData2[-1][-1] * 14)
        avg6 = round(totCap6/3.5)
        avg7 = round(totCap7/3.5)
        free6 = round(avg6 * (100 - tableData[-1][-1])/100)
        free7 = round(avg7 * (100 - tableData[-1][-1])/100)
        totCap6 = round(totCap6)
        totCap7 = round(totCap7)
    except:
        free6 = free7 = avg6 = avg7 = totCap6 = totCap7 = "Unavailable"
    
    """  
    --------------------------------------------------
    Dictionary that template uses to get data from
    --------------------------------------------------
    """

    context = {
        'tableHeaders' : tableHeaders,
        'tableData'    : tableData,
        'tableHeaders2': tableHeaders2,
        'tableData2'   : tableData2,
        'years'        : years,
        'sessions'     : sessions,
        'selectedSession' : session,
        'selectedYear'    : year,
        'totCap6'     : totCap6,
        'totCap7'     : totCap7,
        'avg6'        : avg6,
        'avg7'        : avg7,
        'free6'       : free6,
        'free7'       : free7,
    }

    return render(request, 'resources/resource_usage.html', context)

"""  
--------------------------------------------------------------------------------
For AVAILABILITY AND CCOURSE OFFERING COMPARISON page
--------------------------------------------------------------------------------
"""

def resourceComp(request):
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
                
            SELECT iubResource.Class_Size AS "Class Size", iubResource.nRooms AS "IUB Resource", req.Class_Room_6 AS "Slot 6", (req.Class_Room_6 - iubResource.nRooms) AS "Difference for 6 slots", req.Class_Room_7 AS "Slot 7", (req.Class_Room_7 - iubResource.nRooms) AS "Difference for Slot 7"
            FROM(
                SELECT 20 AS Class_Size, 20 AS nRooms UNION SELECT 30, 3 UNION SELECT 35, 18 UNION SELECT 40, 10 UNION SELECT 50, 34 UNION SELECT 54, 1 UNION SELECT 64, 2 UNION SELECT 124, 3 UNION SELECT 168, 1
                ) AS iubResource	
                INNER JOIN (
                    SELECT ( 
                        CASE 
                            WHEN S.nEnrolled BETWEEN  1 AND 20 THEN 20  
                                WHEN S.nEnrolled BETWEEN 21 AND 30 THEN 30
                                WHEN S.nEnrolled BETWEEN 31 AND 35 THEN 35
                                WHEN S.nEnrolled BETWEEN 36 AND 40 THEN 40
                                WHEN S.nEnrolled BETWEEN 51 AND 54 THEN 54
                                WHEN S.nEnrolled BETWEEN 55 AND 64 THEN 64
                                WHEN S.nEnrolled BETWEEN 65 AND 124 THEN 124
                                WHEN S.nEnrolled BETWEEN 125 AND 168 THEN 168
                                WHEN S.nEnrolled >168 THEN S.nEnrolled
                            ELSE 0  
                        END 
                    ) AS Class_Size, ROUND(COUNT(*)/12, 1) AS Class_Room_6, ROUND(COUNT(*)/14, 1) AS Class_Room_7
                    FROM Section_T S
                    WHERE 
                            dYear= %(year)s 
                        AND eSession = %(session)s
                    GROUP BY Class_Size
                    HAVING Class_Size != 0
                    ORDER BY Class_Size
                ) AS req 
                ON req.Class_Size = iubResource.Class_Size

            UNION

            SELECT "Total", SUM(iubResource.nRooms), SUM(req.Class_Room_6), SUM(req.Class_Room_6 - iubResource.nRooms), SUM(req.Class_Room_7), SUM(req.Class_Room_7 - iubResource.nRooms)
            FROM(
                SELECT 20 AS Class_Size, 20 AS nRooms UNION SELECT 30, 3 UNION SELECT 35, 18 UNION SELECT 40, 10 UNION SELECT 50, 34 UNION SELECT 54, 1 UNION SELECT 64, 2 UNION SELECT 124, 3 UNION SELECT 168, 1
                ) AS iubResource	
                INNER JOIN (
                    SELECT ( 
                        CASE 
                            WHEN S.nEnrolled BETWEEN  1 AND 20 THEN 20  
                                WHEN S.nEnrolled BETWEEN 21 AND 30 THEN 30
                                WHEN S.nEnrolled BETWEEN 31 AND 35 THEN 35
                                WHEN S.nEnrolled BETWEEN 36 AND 40 THEN 40
                                WHEN S.nEnrolled BETWEEN 51 AND 54 THEN 54
                                WHEN S.nEnrolled BETWEEN 55 AND 64 THEN 64
                                WHEN S.nEnrolled BETWEEN 65 AND 124 THEN 124
                                WHEN S.nEnrolled BETWEEN 125 AND 168 THEN 168
                                WHEN S.nEnrolled >168 THEN S.nEnrolled
                            ELSE 0  
                        END 
                    ) AS Class_Size, ROUND(COUNT(*)/12, 1) AS Class_Room_6, ROUND(COUNT(*)/14, 1) AS Class_Room_7
                    FROM Section_T S
                    WHERE 
                            dYear= %(year)s 
                        AND eSession = %(session)s
                    GROUP BY Class_Size
                    HAVING Class_Size != 0
                    ORDER BY Class_Size
                ) AS req 
                ON req.Class_Size = iubResource.Class_Size
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
    
    return render(request, 'resources/resource_comparison.html', context)
