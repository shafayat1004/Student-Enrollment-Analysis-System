--
-- Create model ClassroomT
--
CREATE TABLE `Classroom_T` (`cRoom_ID` char(10) NOT NULL PRIMARY KEY, `nRoomCapacity` integer NULL);
--
-- Create model FacultyT
--
CREATE TABLE `Faculty_T` (`cFaculty_ID` char(4) NOT NULL PRIMARY KEY, `cFacultyName` varchar(50) NULL);
--
-- Create model SchoolT
--
CREATE TABLE `School_T` (`cSchool_ID` char(5) NOT NULL PRIMARY KEY, `cSchoolName` varchar(50) NULL);
--
-- Create model DepartmentT
--
CREATE TABLE `Department_T` (`cDepartment_ID` char(3) NOT NULL PRIMARY KEY, `cDepartmentName` varchar(50) NULL, `cSchool_ID` char(5) NULL);
--
-- Create model CourseT
--
CREATE TABLE `Course_T` (`cCourse_ID` char(7) NOT NULL PRIMARY KEY, `cCourseName` varchar(30) NULL, `nCreditHours` integer NULL, `cDepartment_ID` char(3) NULL);
--
-- Create model CoofferedcourseT
--
CREATE TABLE `CoOfferedCourse_T` (`cCoffCode_ID` char(7) NOT NULL PRIMARY KEY, `cCourse_ID` char(7) NULL);
--
-- Create model SectionT
--
CREATE TABLE `Section_T` (`section_ID` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `eSession` enum('Autumn','Summer','Spring') NOT NULL, `eDays` enum('ST','MW','S','M','T','W','R','F','A') NULL, `dYear` YEAR NOT NULL, `nSectionNumber` integer NULL, `nSectionCapacity` integer NULL, `nEnrolled` integer NULL, `bIsBlocked` bool NULL, `tStartTime` time(4) NULL, `tEndTime` time(4) NULL, `cCoffCode_ID` char(7) NULL, `cFaculty_ID` char(4) NULL, `cRoom_ID` char(10) NULL);
ALTER TABLE `Department_T` ADD CONSTRAINT `Department_T_cSchool_ID_63ec4e50_fk_School_T_cSchool_ID` FOREIGN KEY (`cSchool_ID`) REFERENCES `School_T` (`cSchool_ID`);
ALTER TABLE `Course_T` ADD CONSTRAINT `Course_T_cDepartment_ID_db6f888e_fk_Department_T_cDepartment_ID` FOREIGN KEY (`cDepartment_ID`) REFERENCES `Department_T` (`cDepartment_ID`);
ALTER TABLE `CoOfferedCourse_T` ADD CONSTRAINT `CoOfferedCourse_T_cCourse_ID_978180ee_fk_Course_T_cCourse_ID` FOREIGN KEY (`cCourse_ID`) REFERENCES `Course_T` (`cCourse_ID`);
ALTER TABLE `Section_T` ADD CONSTRAINT `Section_T_cCoffCode_ID_eSession_dY_32461251_uniq` UNIQUE (`cCoffCode_ID`, `eSession`, `dYear`, `nSectionNumber`);
ALTER TABLE `Section_T` ADD CONSTRAINT `Section_T_cCoffCode_ID_a2585c57_fk_CoOffered` FOREIGN KEY (`cCoffCode_ID`) REFERENCES `CoOfferedCourse_T` (`cCoffCode_ID`);
ALTER TABLE `Section_T` ADD CONSTRAINT `Section_T_cFaculty_ID_a3346fb8_fk_Faculty_T_cFaculty_ID` FOREIGN KEY (`cFaculty_ID`) REFERENCES `Faculty_T` (`cFaculty_ID`);
ALTER TABLE `Section_T` ADD CONSTRAINT `Section_T_cRoom_ID_dd113d5d_fk_Classroom_T_cRoom_ID` FOREIGN KEY (`cRoom_ID`) REFERENCES `Classroom_T` (`cRoom_ID`);