from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse


# Create your views here.
def schoolRevenue( request ):

    labels = []
    data = []

    query = """
            SET @sql = NULL;
            SELECT GROUP_CONCAT(
                CONCAT( 
                    'SUM( CASE WHEN E.School = "', S.sch, '" THEN Revenue ELSE 0 END ) AS ', S.sch 
                ) SEPARATOR ", "
            ) INTO @sql
            FROM (
                SELECT cSchool_ID AS sch
                FROM School_T
            ) S;

            SET @sql = CONCAT(
                "
                SELECT 
                    CONCAT( Years, ' ',  Sessions ) AS ' ',
                    ", @sql, ",
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
                "
            );

            PREPARE stmt FROM @sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
            """

    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()
        

    return render( request, "revenue.html", { 
            'labels': labels,
            'data': data,
        }
    )


def iubRevenue( request ):

    labels = []
    data = []

    query = """
            SELECT 
                dYear AS Years, 
                eSession AS Sessions
            FROM Section_T
            GROUP BY dYear, eSession
            ORDER BY dYear ASC, eSession DESC; CHANGE ALL OF THIS
            """

    with connection.cursor() as cursor:
        cursor.execute( query )
        labels = [ col[0] for col in cursor.description ]
        data = cursor.fetchall()
        

    return render( request, "revenue.html", { 
            'labels': labels,
            'data': data,
        }
    )