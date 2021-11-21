INSERT INTO School_T (cSchool_ID, cSchoolName)
VALUES (
    'SETS',
    'School Of Engineering, Technology And Sciences'
  );


INSERT INTO Department_T (cDepartment_ID, cDepartmentName, cSchool_ID)
VALUES (
    'CSE',
    'Computer Science And Engineering',
    'SETS'
  );


INSERT INTO Course_T (
    cCourse_ID,
    cCourseName,
    nCreditHours,
    cDepartment_ID
  )
VALUES (
    'CSE303',
    'Database Management',
    '3',
    'CSE'
  );



INSERT INTO CoOfferedCourse_T (cCoffCode_ID, cCourse_ID)
VALUES (
    'CEN401',
    'CSE303'
  );


INSERT INTO Faculty_T (cFaculty_ID, cFacultyName)
VALUES (
    '8000',
    'MR. Faculty'
  );


INSERT INTO Classroom_T (cRoom_ID, nRoomCapacity)
VALUES (
    'ROOM10',
    '50'
  );


INSERT INTO Section_T (
    dYear,
    nSectionNumber,
    nSectionCapacity,
    nEnrolled,
    bIsBlocked,
    tStartTime,
    tEndTime,
    eDays,
    eSession,
    cCoffCode_ID,
    cFaculty_ID,
    cRoom_ID
  )
VALUES (
    '2021',
    2,
    '50',
    '20',
    '0',
    '14:00',
    '15:30',
    'ST', 
    'Autumn',
    'CEN401',
    '8000',
    'ROOM10'
  );