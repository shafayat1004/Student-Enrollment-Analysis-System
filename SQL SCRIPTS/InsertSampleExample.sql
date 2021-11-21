INSERT INTO database_school (cSchool_ID, cSchoolName)
VALUES (
    'SETS',
    'School Of Engineering, Technology And Sciences'
  );


INSERT INTO database_department (cDepartment_ID, cDepartmentName, cSchool_ID_id)
VALUES (
    'CSE',
    'Computer Science And Engineering',
    'SETS'
  );


INSERT INTO database_course (
    cCourse_ID,
    cCourseName,
    nCreditHours,
    cDepartment_ID_id
  )
VALUES (
    'CSE303',
    'Database Management',
    '3',
    'CSE'
  );



INSERT INTO database_coofferedcourse (cCoffCode_ID, cCourse_ID_id)
VALUES (
    'CEN401',
    'CSE303'
  );


INSERT INTO database_faculty (cFaculty_ID, cFacultyName)
VALUES (
    '8000',
    'MR. Faculty'
  );


INSERT INTO database_classroom (cRoom_ID, nRoomCapacity)
VALUES (
    'ROOM10',
    '50'
  );


INSERT INTO database_section (
    dYear,
    nSectionNumber,
    nSectionCapacity,
    nEnrolled,
    bIsBlocked,
    tStartTime,
    tEndTime,
    eDays,
    eSession,
    cCoffCode_ID_id,
    cFaculty_ID_id,
    cRoom_ID_id
  )
VALUES (
    '2021',
    2,
    '50',
    '20',
    '0',
    '14:00',
    '15:30',
    -- TODO there is an error here "WARN_DATA_TRUNCATED: Data truncated for column 'eDays' at row 1"
    'St', 
    'Autumn',
    'CEN401',
    '8000',
    'ROOM10'
  );