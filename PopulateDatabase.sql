-- AUTO-GENERATED QUERY FROM populateALLTables FUNCTION


-- Populating Classroom_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE Classroom_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@d,@d,@d,@d,@d,@d,@d,@d,@ROOM_ID,@ROOM_CAPACITY,@d,@d,@d,@d,@d,@d,@d,@d) 
SET cRoom_ID=@ROOM_ID,nRoomCapacity=@ROOM_CAPACITY;


-- Populating Faculty_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE Faculty_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d) 
SET cFaculty_ID=@FACULTY_ID,cFacultyName=@FACULTY_NAME;


-- Populating School_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE School_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@SCHOOL_TITLE,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d) 
SET cSchool_ID=@SCHOOL_TITLE,cSchoolName=@SCHOOL_NAME;


-- Populating Department_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE Department_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@SCHOOL_TITLE,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d) 
SET cDepartment_ID=@DEPARTMENT_ID,cDepartmentName=@DEPARTMENT_NAME,cSchool_ID=@SCHOOL_TITLE;


-- Populating Course_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE Course_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@d,@COFFER_COURSE_ID,@d,@d,@CREDIT_HOUR,@d,@d,@d,@d,@d,@d,@COURSE_NAME,@d,@d,@d,@d,@d,@d) 
SET cCourse_ID=@COFFER_COURSE_ID,cCourseName=@COURSE_NAME,nCreditHours=@CREDIT_HOUR,cDepartment_ID=@DEPARTMENT_ID;


-- Populating CoOfferedCourse_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE CoOfferedCourse_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@d,@COFFER_COURSE_ID,@COFFERED_WITH,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d,@d) 
SET cCoffCode_ID=@COFFERED_WITH,cCourse_ID=@COFFER_COURSE_ID;


-- Populating Section_T
LOAD DATA LOCAL
INFILE "/home/shafayat/Coding/django/2021 Summer and Spring original.csv" 
INTO TABLE Section_T 
FIELDS TERMINATED BY ","
IGNORE 1 LINES 
(@d,@COFFER_COURSE_ID,@d,@SECTION,@d,@CAPACITY,@ENROLLED,@d,@ROOM_ID,@d,@BLOCKED,@d,@d,@d,@END_TIME,@ST_MW,@Year,@Semester) 
SET eSession=@Semester,eDays=@ST_MW,dYear=@Year,nSectionNumber=@SECTION,nSectionCapacity=@CAPACITY,nEnrolled=@ENROLLED,bIsBlocked=@BLOCKED,tStartTime=@START_TIME,tEndTime=@END_TIME,cCoffCode_ID=@COFFER_COURSE_ID,cFaculty_ID=@FACULTY_ID,cRoom_ID=@ROOM_ID;


