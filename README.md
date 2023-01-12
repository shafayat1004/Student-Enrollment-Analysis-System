#### Project Videos
Longer (Older Video)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/JD5bnZqs2-8/0.jpg)](https://youtu.be/JD5bnZqs2-8)

Latest (Shorter Video)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/olExNtIXbC8/0.jpg)](https://youtu.be/olExNtIXbC8)

# Setup

1.  Clone the repository

1.  On Linux :
    ```bash
    python3 -m venv path/to/Student-Enrollment-Analysis-System
    ```
1.  On Windows, invoke the venv command as follows:
    ```ps
    c:\>c:\Python35\python -m venv c:\path\to\myenv
    ```
    Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:
    ```ps
    c:\>python -m venv c:\path\to\myenv
    ```
1.  ```
    cd path/to/Student-Enrollment-Analysis-System
    ```
1.  On Linux:
    ```bash
    source bin/activate
    ```
1.  On Windows cmd:
    ```cmd
    Scripts\activate.bat
    ```
    powershell:
    ```ps
    Scripts\Activate.ps1
    ```
1.  ```
    pip install -r requirements.txt
    ```
1.  Install MySQL Community Server:
1.  In MySQL as root/admin:
    ```
    CREATE DATABASE SEAS_Database;
    CREATE USER 'djangouser'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345';
    GRANT ALL ON SEAS_Database.* TO 'djangouser'@'localhost';
    FLUSH PRIVILEGES;
    ```
1.  In the SEAS folder:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
1.  Navigate to the webpage, use superuser credentials.
1.  Populate database.
1.  Make sure the XLSX file is in the format:

    |SCHOOL_TITLE|COFFERED_WITH|SECTION|CREDIT_HOUR|CAPACITY|ENROLLED|ROOM_ID|ROOM_CAPACITY|BLOCKED|COURSE_NAME|FACULTY_FULL_NAME|START_TIME|END_TIME|ST_MW|DEPARTMENT_ID|ClassSize|stuCr|Year|Semester|
    |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|











<img src="media/image1.png" style="width:3.32292in;height:2.78125in" />

**INDEPENDENT UNIVERSITY, BANGLADESH**

> **Course**: Database Management (CSE303)
>
> **Section:** 04

**Semester:** Autumn 2021

**Student Enrollment Analysis System (SEAS)**

**<u>SUBMITTED BY:</u>**

Mir Shafayat Ahmed (1910456)

Suhaila (1910496)

Fahim Ahmed (2022409)

Dewan Wakil Ahmed (1921166)

Ariful Islam Shiam (1710864)

Ahmad Reyad Onik (1710284)

**<u>SUBMITTED TO:</u>**

Ms. Sadita Ahmed

Lecturer

Department of Computer Science & Engineering

*Date of Submission: 31<sup>st</sup> October, 2021*

# **Table of Contents**

## [Chapter 1: Introduction](#chapter-1-introduction)

[A. Background of the Organization](#background-of-the-organization)

[B. Background of the Project](#background-of-the-project)

[C. Objectives of the Project](#objectives-of-the-project)

[D. Scope of the Project](#scope-of-the-project)

## [Chapter 2: Requirement Analysis](#chapter-2-requirement-analysis)

[A. Rich Picture - Existing System](#_Toc91299041)

[B. Six Elements Analysis - Existing System](#six-elements-analysis---existing-system)

[C. Business Process Model and Notation 2.0 – Existing System](#business-process-model-and-notation-2.0-existing-system)

[D. Problem Analysis – Existing System](#d.-problem-analysis-existing-system)

[D. Rich Picture - Proposed System](#rich-picture---proposed-system)

[E. Six Elements Analysis - Proposed System](#six-elements-analysis---proposed-system)

[F. BUsiness Process Model and Notation 2.0 – Proposed System](#business-process-model-and-notation-2.0-proposed-system)

## [Chapter 3: Logical System design](#chapter-3-logical-system-design)

[A. Business Rules](#business-rules)

[B. ERD](#erd)

[C. Relational Schema](#relational-schema)

[D. Normalization](#normalization)

[E. Datat Dictionary](#data-dictionary)

## [Chapter 4: Physical System Design](#chapter-4-physical-system-design)

[A. Input Forms](#input-forms)

[B. Output Query & Reports](#output-query-reports)

## [Chapter 5: Conclusion](#chapter-5-conclusion)

[A. Problems and solution](#problems-and-solution)

[B. Additional feature and future development](#b.-additional-feature-and-future-development)

## [References](#_Toc91299060)

## Figures

[Figure 1 Rich Picture of Existing System](#_Toc91299061)

[Figure 2 Prepare Classroom Requirement list for different
Sections](#_Toc91299062)

[Figure 3 Prepare tally sheet](#_Toc91299063)

[Figure 4 Generate "Dept. Revenue and Change %" chart](#_Toc91299064)

[Figure 5 Generate School revenue table and chart](#_Toc91299065)

[Figure 6 Generate “School class size distribution
chart”](#_Toc91299066)

[Figure 7 Prepare IUB Revenue Distribution related Charts and
Tables](#_Toc91299067)

[Figure 8 Prepare Resource Related Charts and Tables](#_Toc91299068)

[Figure 9 Revise room assignment](#_Toc91299069)

[Figure Rich Picture of Proposed System](#_Toc91299070)

[Figure Prepare Classroom Requirement list for different
Sections](#_Toc91299071)

[Figure Upload Tally Sheet](#_Toc91299072)

[Figure View all School and department related Revenue tables and
charts.](#_Toc91299073)

[Figure View IUB revenue table and charts.](#_Toc91299074)

[Figure View class size distribution data for schools](#_Toc91299075)

[Figure View resource requirement and usage data](#_Toc91299076)

[Figure Revise Room Assignment](#_Toc91299077)

[Figure 18 ERD](#_Toc91299078)

[Figure 19 Relational Schema](#_Toc91299079)

# Chapter 1: Introduction

##  Background of the Organization

Independent University, Bangladesh (IUB) is one of the premier private
higher education institutions in the country. With 8,423 students
currently enrolled, 13,745 alumni, and 401 faculty members, IUB aims to
produce world-class graduates as well as being at the forefront of
cutting-edge research in diverse fields ranging from Computer Science to
Public Health \[1\]. Currently, the University has 6 academic schools:

-   School of Business

-   School of Engineering and Computer Science

-   School of Environmental Sciences and Management

-   School of Liberal Arts and Social Sciences

-   School of Life Sciences

-   School of Public Health

The School of Architecture and the School of Biotechnology are in the
process of being added to its rapidly growing portfolio. Apart from the
spacious campus, well-equipped laboratories, and enormous library, the
university offers its students generous scholarships - both academic and
need-based - so that they can get the opportunity to gather the
necessary knowledge and expertise to be well equipped for their future
careers.

##  Background of the Project

A university the size of IUB generates an enormous amount of enrollment
data every semester. Analyzing this data is a mammoth task for the
people whose job it is to process this data into a form that the higher
authorities can use to better inform their decision-making. It is a
tedious process from start to finish, involving a great deal of
error-prone and time-consuming manual labor.

Enter the Student Enrollment Analysis System (SEAS). We aim to eliminate
this slow, monotonous process entirely with the use of computerized
automation. We propose that the enrollment data should be stored in the
Student Enrollment Analysis System’s accompanying database. SEAS will
process this data without the need for human intervention and generate,
on-demand, the various charts and tables the management and stakeholders
at IUB require to accomplish their task of running the university
efficiently. The outcome - employees will be freed up to pursue more
urgent and meaningful tasks and the higher authorities have instant
access to all the data they need access to only a few mouse clicks away.

Overall, SEAS will save Independent University, Bangladesh precious
time, money, and resources that can be better utilized towards its
primary goal of providing the best education possible to the students
who make this institution so special.

## Objectives of the Project

The main intention of our project is to provide software whose basic
function will be to generate information such as total student
enrollment both school wise and department wise, enrollment wise course
distribution among those schools, IUB resource usage based on
enrollment, i.e., classroom requirement, course distribution per
semester of different schools and departments. All these essential data
can be retrieved without much need of human interference in establishing
a useful final product. This will enhance efficiency and productivity
among individuals in need of such valuable information through this
software enabling easy data access which in turn reduces manual labor
leading to fewer human errors.

However, to build such a system, the cost might be initially high, but
in the long run, the cost is relatively low compared to the cost
incurred in doing this same data retrieval process manually. Moreover,
as the process becomes automated, less time will be invested and thus
individuals can focus on other manual jobs. In addition, this automated
system of data retrieval process provides little/no room for human
errors, and thus, the quality of the work produced is enhanced
eliminating potential costs.

##  Scope of the Project

Following a thorough examination of the present system, we discovered
areas in the business processes that can create significant delays in
time and communication, which we will examine in the following chapter.

Our proposed solution is to create a Student Enrollment Analysis System
(SEAS) which will be a web application with a centralized database that
will be using a Relational Database Management System (RDMS) called
MySQL. It will be able to store, edit, add and update necessary data for
auto-generating accurate reports with charts and tables. Detailed
Analysis of the Student Enrollment in terms of availability and
utilization of IUB resources, and the revenue generated in each semester
will be available for viewing.

The proposed system will be able to handle the extraction of newly
aggregated data and add them to the relevant relational tables, in a
highly organized manner from uploaded tally-sheet spreadsheet files.
Then the system will be able to perform all the necessary calculations
for generating preferred charts and tables based on the user request
preference.

A user interface will be designed and connected to the database that
will serve as a portal of the web application for the users to log in
and see what types of reports are available for viewing. These reports
will be designed following the guidelines outlined in the functional
requirements.

# Chapter 2: Requirement Analysis

## Rich Picture - Existing System 

<img src="media/image2.png" style="width:5.98734in;height:4.95909in" />

<span id="_Toc91299061" class="anchor"></span>Figure 1 Rich Picture of
Existing System

##  Six Elements Analysis - Existing System

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Process</strong></td>
<td colspan="6"><strong>System Roles</strong></td>
</tr>
<tr class="even">
<td><strong>Human</strong></td>
<td><strong>Non-Computing Hardware</strong></td>
<td><strong>Computer Hardware</strong></td>
<td><strong>Software</strong></td>
<td><strong>Database</strong></td>
<td><strong>Network &amp; Communication</strong></td>
</tr>
<tr class="odd">
<td><strong>Prepare Classroom Requirement list for different sections</strong></td>
<td><p><strong>Department Office Manager:</strong></p>
<p>1. Each department retrieves their previous semester’s enrollment data.</p>
<p>2. After analyzing the previous semester data, prediction is done on the number of sections and classrooms needed for the new semester.</p>
<p>3. New section list is created based on the prediction.</p>
<p>4. Along with it the expected classroom requirement list is created.</p>
<p>4. The new lists are sent to the registrar’s office.</p>
<p>5.Meanwhile, the files are also stored in the archive.</p>
<p><strong>Registrar’s office:</strong></p>
<p>1. Receives the classroom requirement and section files from respective departments.</p>
<p>2. Compiles all the section lists and classroom requirements from all departments.</p>
<p>3. Stores in the archive.</p>
<p>4. Uploads list to iRAS</p></td>
<td><p><strong>Pen &amp; paper:</strong></p>
<p>1. Department will use pen and paper to analyze previous semester data.</p>
<p>2. To create drafts of section assignments.</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. Department uses a computer to analyze data, to create sections.</p>
<p>2. Department sends a list to the registrar office.</p>
<p><strong>Printer:</strong></p>
<p>1.Department uses a printer to print the list for future use.</p></td>
<td><p><strong>Microsoft Office:</strong></p>
<p>1. Microsoft Excel will be used to make section lists.</p>
<p><strong>Gmail:</strong></p>
<p>1. Gmail will be used to send the file to the registrar office.</p></td>
<td><p><strong>Spreadsheet:</strong></p>
<p>1. It will be used to store datasheets for the future.</p>
<p><strong>Archive:</strong></p>
<p>1. Stores both softcopy and hardcopy of the spreadsheet.</p></td>
<td><p><strong>Internet:</strong></p>
<p>1. Internet must be needed for all the process</p></td>
</tr>
<tr class="even">
<td><strong>Prepare tally sheet</strong></td>
<td><p><strong>Registrar’s Office:</strong></p>
<p>1. Logs into the iRAS.</p>
<p>2.Downloads the enrollment data after student registration is completed.</p>
<p>3.Separate data according to department </p>
<p>4.Stores the enrollment data in excel file.</p>
<p>5.Keeps the file in the archive.</p>
<p>5.Sends the department-wise compiled enrollment data to respective department via email.</p></td>
<td><p><strong>Paper</strong>:</p>
<p>1.Needed for printing the hardcopy of enrollment data.</p>
<p><strong>Store Room:</strong></p>
<p>1.Used to store the physical hardcopy file in the office.</p></td>
<td><p><strong>Computer:</strong></p>
<p>1.Used for accessing iRAS.</p>
<p><strong>Printer:</strong></p>
<p>1.To print a hard copy of the tally sheet.</p></td>
<td><p><strong>Microsoft Excel:</strong></p>
<p>1.To be able to view the data (tally sheet)</p>
<p><strong>Gmail:</strong></p>
<p>1.Used to send the tally sheet soft copy to the concerned department.</p>
<p><strong>iRAS:</strong></p>
<p>1.To have access to enrollment data. Users can download the enrollment data from here. </p></td>
<td><p><strong>Archive:</strong></p>
<p>1.Stores both softcopy and hardcopy of the excel file.</p>
<p><strong>Spreadsheet:</strong></p>
<p>1.Stores enrollment data which are downloaded from iRAS.</p></td>
<td><p><strong>Internet:</strong></p>
<p>1.Used by- the registrar’s office to access iRAS.</p>
<p>2. For sending files through email.</p></td>
</tr>
<tr class="odd">
<td><strong>Generate "Dept. Revenue and Change %" chart</strong></td>
<td><p><strong>Department Offices:</strong></p>
<p>1. Each department receives its tally sheet from the Registrar's Office.</p>
<p>2. From the tally sheet, the number of enrolled students in a section is multiplied by credit hour to give student credits in that section.</p>
<p>3. Adds up the student credits of every section of each course (of that department).</p>
<p>4. Retrieves previous semester revenue table from department archive</p>
<p>5. Updates the table with this semester’s calculated revenue</p>
<p>6. Uses the updated table to calculate the line of best fit for revenue.</p>
<p>7 Calculate percentage change in revenue compared to previous semester.</p>
<p>8. Plot :</p>
<p>i. revenue data against the semester.</p>
<p>ii. line of best fit for revenue</p>
<p>iii. percentage change in revenue</p>
<p>9. Send prepared documents to:</p>
<p>i. the department archive for storage</p>
<p>ii. the school this department belongs to, for further processing</p>
<p>10. Notify school that documents have been sent</p></td>
<td><p><strong>Pen and Paper:</strong></p>
<p>1. Used to sign off the prepared charts and tables before being sent off to the school.</p>
<p>2. Charts and tables printed on paper for viewing and sent to school.</p>
<p>3. Printed hardcopy of data is kept in storage</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. For viewing and processing the tally-sheet into the table and chart</p>
<p><strong>Printer:</strong></p>
<p>1. Prints the hardcopies for storage and viewing</p></td>
<td><p><strong>Microsoft Excel:</strong></p>
<p>1. Tally sheet is an Excel sheet.</p>
<p>2. All processing, calculation, and generation is done using Excel’s features</p>
<p><strong>Gmail:</strong></p>
<p>1. Accessed via web browser.</p>
<p>2. Tally sheet received via e-mail from the registrar's office.</p>
<p>3. Backup copy of processed documents emailed to school, along with the hardcopy.</p></td>
<td><p><strong>Local Archive Room:</strong></p>
<p>1. Department stores its processed data and output documents in their archive for long-term recordkeeping.</p>
<p><strong>Local Computer Storage:</strong></p>
<p>1. Data files remain in the employee’s work computer for some time after being worked on.</p>
<p><strong>Google Drive:</strong></p>
<p>1. All files emailed from Gmail are saved in the cloud automatically.</p></td>
<td><p><strong>Internet:</strong></p>
<p>1. For communication and coordination between the offices.</p>
<p>2. For receiving the tally sheet from the Registrar.</p>
<p>3. For sending the processed output to the school.</p>
<p><strong>Intercom:</strong></p>
<p>1. For quick communication between offices.</p>
<p>2. For notifying schools that documents have been sent</p></td>
</tr>
<tr class="even">
<td><strong>Generate School revenue table and chart</strong></td>
<td><p><strong>School:</strong></p>
<p>1. Receives revenue tables and charts from all of its departments</p>
<p>2. Merge all the revenue data sheets to create the school’s revenue table.</p>
<p>3. Sum department revenues to calculate school revenue.</p>
<p>4. Calculate change in revenue for each department and for the school overall versus the same semester of the previous academic year.</p>
<p>5. Plot department-wise revenue trend line chart.</p>
<p>6. Plot school revenue distribution area chart.</p>
<p>7. Send the charts and tables to :</p>
<p>i. the core analysis team for further processing.</p>
<p>ii. Archive for storage</p>
<p>8. Notify the core analysis team via intercom that documents have been sent.</p></td>
<td><p><strong>Pen and Paper:</strong></p>
<p>1. Used to sign, approve and keep the hard copy of documents.</p>
<p>2. To view, charts and tables are printed on paper.</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. To arrange, merge, process, calculate and make simplified charts collected data sheets.</p>
<p><strong>Printer:</strong></p>
<p>1. Hardcopies are printed for storage and viewing.</p></td>
<td><p><strong>MS Excel:</strong></p>
<p>1. Tables and chart softcopies are in Excel sheets.</p>
<p>2. All processes, calculation, chart generation etc. are done using Excel’s features.</p>
<p><strong>Gmail:</strong></p>
<p>1. Accessed via web browser.</p>
<p>2. File sending and some communication between parties occur via email</p></td>
<td><p><strong>Local Archive Room:</strong></p>
<p>1. For long-term record keeping of the documents generated.</p>
<p><strong>Local Computer Storage:</strong></p>
<p> 1. After being worked on, files remain on the employee's work computer for a period of time.</p>
<p><strong>Google Drive:</strong></p>
<p>1. All files emailed from Gmail are saved in the cloud and shared using gdrive</p></td>
<td><p><strong>Internet:</strong></p>
<p>1. For inter-office communication and collaboration</p>
<p>2. For transferring and receiving the documents.</p>
<p><strong>Intercom:</strong></p>
<p>1. For quick communication between offices.</p>
<p>2. For notifying schools that documents have been sent</p></td>
</tr>
<tr class="odd">
<td><strong>Generate School Class Size Distribution chart</strong></td>
<td><p><strong>School:</strong></p>
<p>1. Receives enrollment-wise class size distribution related data and charts from all of its departments.</p>
<p>2. Merge all the data sheets to create the school’s class size distribution table.</p>
<p>3. Sum department class sizes distribution to calculate school class size distribution.</p>
<p>5. Plot department-wise class size distribution chart.</p>
<p>6. Plot school class size distribution chart.</p>
<p>7. Send the chart:</p>
<p>i. the core analysis team for further processing.</p>
<p>ii. Archive for storage</p>
<p>8. Notify the core analysis team via intercom that documents have been sent.</p></td>
<td><p><strong>Pen and paper:</strong></p>
<p>1.School senior manager uses pen and paper to create a draft for class size distribution.</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. School senior manager will use a computer to create their chart.</p></td>
<td><p><strong>MS Excel:</strong></p>
<p>1. Tables and chart softcopies are in Excel sheets.</p>
<p>2. All processes, calculation, chart generation etc. are done using Excel’s features.</p>
<p><strong>Gmail:</strong></p>
<p>1. File sending and some communication to notify via email</p></td>
<td><p><strong>Spreadsheet:</strong></p>
<p>1. This sheet will be used for Reserve data for the future.</p></td>
<td><p><strong>Internet:</strong></p>
<p>1. For inter-office communication and collaboration</p>
<p>2. For transferring and receiving the documents.</p>
<p><strong>Intercom:</strong></p>
<p>1. For quick communication between offices.</p>
<p>2. For notifying schools that documents have been sent</p></td>
</tr>
<tr class="even">
<td><strong>Prepare IUB Revenue Distribution related Charts and Tables</strong></td>
<td><p><strong>Core Analysis Team:</strong></p>
<p>1. Receives school-specific revenue charts and tables from the respective schools.</p>
<p>3. Compile total revenue of individual schools in a table.</p>
<p>4. Calculates the IUB total revenue for each semester.</p>
<p>5.Calculates % change in revenue over previous year for each semester.</p>
<p>6. Generate “Revenue Distribution Among Schools” charts from prepared table</p>
<p>6. Generate “Revenue Trend of The Schools” charts from prepared table</p>
<p>7. Generate “Revenue And % Change” charts from prepared table</p>
<p>8. Prepares Presentation for other stakeholders out of the prepared charts and tables.</p></td>
<td><p><strong>Paper Documents &amp; Envelopes: </strong></p>
<p>1. Printed paper documents are exchanged between the offices of the department heads, deans, core analysis team &amp; the higher authority in carefully signed and sealed envelopes.</p>
<p><strong>Office Stationeries:</strong></p>
<p>1. In each of the above-mentioned offices, stationeries like pens, pencils, erasers, highlighters, markers, staplers, folders etc. are used to edit for corrections to prepare and send these documents to the required offices.</p></td>
<td><p><strong>Computers: </strong></p>
<p>1. Computers are used to produce and make final modifications from the corrected revenue report paper documents.</p>
<p>2. Open and view received revenue report documents from other offices. </p>
<p><strong>Printers: </strong></p>
<p>1. Print paper documents of the revenue reports.</p>
<p><strong>Networking Devices: </strong></p>
<p>1. Networking devices like WiFi-routers, extenders and as such are used to exchange the soft-copies of the revenue report documents between the offices via email.</p></td>
<td><p><strong>Microsoft Excel:</strong></p>
<p>1. Perform relevant calculations on the aggregate d raw revenue data. 2. Prepare charts and tables for the revenue reports from the processed aggregated raw data. </p>
<p><strong>Microsoft Word: </strong></p>
<p>1. Write up revenue reports and include the generated charts and tables from MS-Excel. </p>
<p>2. Edit received soft-copies of the revenue reports from other offices. </p>
<p><strong>Adobe Acrobat: </strong></p>
<p>1. Convert revenue reports from doc to pdf files for better viewing across all kinds of devices. </p>
<p>2. Open and view received revenue reports from other offices.</p>
<p><strong>Email: </strong></p>
<p>1. Soft-copies are sent and received between offices via gmail services registered and set up under the IUB domain. </p></td>
<td><p><strong>Distributed Spreadsheet Files:</strong></p>
<p> 1. Revenue data from departments and schools are aggregated and stored in spreadsheet files in a distributed fashion in csv or xlsx formats. </p>
<p><strong>Physical Filing System: </strong></p>
<p>1. Past and current revenue reports are stored as printed hardcopy documents for future use in an organized fashion in each of the offices.</p></td>
<td><p><strong>Internet: </strong></p>
<p>1. Exchanging emails with attached soft-copies of the revenue report documents between the offices requires a stable internet connection.</p>
<p><strong>Intercom-Network: </strong></p>
<p>1. A network of intercoms within the whole IUB premise connects the offices that allows instant voice intercommunication between these offices.</p></td>
</tr>
<tr class="odd">
<td><strong>Prepare Resource Related Charts and Tables</strong></td>
<td><p><strong>Core Analysis Team:</strong></p>
<p>1. Receives files from all school senior managers.</p>
<p>2. Combines all schools’ section enrollment for the current semester (incremented by 1) data in one single table with total for each enrollment category across schools and a final total for number of sections.</p>
<p>3. Groups the Increment-by-one table for all schools and creates the “Enrollment-wise course distribution among the schools” Table</p>
<p>4. Makes the class size distribution chart from the grouped enrollment-wise course distribution table.</p>
<p>5. Make the “Classroom Requirement as per course offering” Table and Pie Chart from the Enrollment table (Increment 1)</p>
<p>6. Make “Usage of the resources” Table from Enrollment table (Increment 1)</p>
<p>7. Makes “IUB Available Resources” table from “Usage of the resources table and existing information about IUB rooms from Registrar.</p>
<p>8. Makes “Availability and course offering comparison” table and “Resource Utilization” chart from “Classroom requirement as per course offering” and “IUB Available Resource”</p>
<p>9. Sends all created files in steps 5, 6, 7, 8 to registrar for room revisions</p>
<p>10. Prepares Presentation for other stakeholders out of the prepared charts and tables.</p></td>
<td><p><strong>Memo:</strong></p>
<p>To distribute non-urgent, yet authoritative, relevant information.</p></td>
<td><p><strong>Computer:</strong></p>
<p>To open and manipulate the received files.</p>
<p><strong>Printer:</strong></p>
<p>To print the charts and tables for viewing.</p>
<p><strong>Networking Devices:</strong></p>
<p>To be able to receive the files from the school.</p></td>
<td><p><strong>Microsoft Excel:</strong></p>
<p>To use formulas and on the raw data and make charts</p>
<p><strong>Microsoft PowerPoint:</strong></p>
<p>To show findings to the stakeholders in a presentable way.</p></td>
<td><p><strong>Spreadsheet:</strong></p>
<p>The file type that is used to store and manipulate real-world data.</p>
<p><strong>Archive:</strong></p>
<p>Findings would be archived for later use</p></td>
<td><p><strong>Internet:</strong></p>
<p>To send digital files across computing devices.</p>
<p><strong>Intercom:</strong></p>
<p>To quickly communicate relevant information across the campus.</p></td>
</tr>
<tr class="even">
<td><strong>Revise room assignment</strong></td>
<td><p><strong>Registrar’s office:</strong></p>
<p>1. Receives all the classroom requirement and usage of resources related charts and tables from Core Analysis Team</p>
<p>2. Updates classroom assignments for sections based on surplus and deficit data of “Resource availability and course offering comparison”</p>
<p>3. stores latest classroom assignment for sections in archive</p>
<p>4. Updates iRAS</p></td>
<td><p><strong>Paper:</strong></p>
<p>1. For printing the hardcopy of the revised room assignment.</p>
<p><strong>Pen:</strong></p>
<p>1. Finalize room distribution by signing on the hardcopy.</p></td>
<td><p><strong>Computer</strong></p>
<p>1. To revise the room distribution data.</p>
<p><strong>Printer:</strong></p>
<p>1.To print the hardcopy of the room distribution data.</p></td>
<td><p><strong>Web-Browser</strong></p>
<p>1. Lets the user have access to iRAS</p>
<p><strong>Gmail:</strong></p>
<p>1.To receive files from core team.</p>
<p><strong>Microsoft Excel:</strong></p>
<p>1. Manipulate the existing classroom assignment.</p>
<p> </p></td>
<td><p><strong>Archive:</strong></p>
<p>1. Stores both softcopy and hardcopy of the spreadsheet.</p></td>
<td><p><strong>Internet: </strong></p>
<p>1. Used for communication through email for sending and receiving files.</p></td>
</tr>
</tbody>
</table>

## Business Process Model and Notation 2.0 – Existing System

<img src="media/image3.png" style="width:6.8148in;height:4.06059in" />

<span id="_Toc91299062" class="anchor"></span>Figure 2 Prepare Classroom
Requirement list for different Sections

<img src="media/image4.png" style="width:6.76116in;height:2.84375in" />

<span id="_Toc91299063" class="anchor"></span>Figure 3 Prepare tally
sheet

<img src="media/image5.png" style="width:6.77695in;height:3.42722in" />

<span id="_Toc91299064" class="anchor"></span>Figure 4 Generate "Dept.
Revenue and Change %" chart

<img src="media/image6.png" style="width:6.76675in;height:1.93786in" />

<span id="_Toc91299065" class="anchor"></span>Figure 5 Generate School
revenue table and chart

<img src="media/image7.png" style="width:6.75316in;height:1.72886in" />

<span id="_Toc91299066" class="anchor"></span>Figure 6 Generate “School
class size distribution chart”

<img src="media/image8.png" style="width:6.62105in;height:2.33684in" />

<span id="_Toc91299067" class="anchor"></span>Figure 7 Prepare IUB
Revenue Distribution related Charts and Tables

<img src="media/image9.png" style="width:6.56757in;height:3.55784in" />

<span id="_Toc91299068" class="anchor"></span>Figure 8 Prepare Resource
Related Charts and Tables

<img src="media/image10.png" style="width:6.59839in;height:2.04717in" />

<span id="_Toc91299069" class="anchor"></span>Figure 9 Revise room
assignment

## D. Problem Analysis – Existing System

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Process Name</strong></td>
<td><strong>Stakeholders</strong></td>
<td><strong>Concerns (Problems)</strong></td>
<td><strong>Analysis (Reason of the Problems)</strong></td>
<td><strong>Proposed Solution</strong></td>
</tr>
<tr class="even">
<td><strong>Prepare Classroom Requirement list for predicted Sections</strong></td>
<td><p>1. Department Office</p>
<p>2. Registrar</p></td>
<td><p>Predictions may be inaccurate.</p>
<p>Making the charts used to make these predictions take a lot of time beforehand</p></td>
<td><p>Predictions made by humans are manually done. So, chances of human prone errors are very high.</p>
<p>Even Though the process is not much long, delays can occur during the department level processing as they might have other more tasks at hand.</p></td>
<td>System will be automatically calculating the previous data. This will eliminate human error from the equation. Therefore, the user can trust the calculation and make more accurate predictions.</td>
</tr>
<tr class="odd">
<td><strong>Prepare tally sheet</strong></td>
<td><p>1.Registrar’s Office</p>
<p>2. Department Office</p></td>
<td><p>Menial labor; requires time.</p>
<p>Hassle of sending paperwork to departments</p>
<p>Data may not get sent on time.</p>
<p>Errors introduced in the tally sheet.</p></td>
<td><p>Has to be manually done by an employee so takes a lot of time whereas the time can be utilized on other tasks.</p>
<p>The Registrar's office has other tasks at hand that may delay this.</p>
<p>Large amount of data so requires time to process thus there might be a delay in sending the file. Even if a long time is taken, human prone errors are not negligible</p></td>
<td><p>Our system can take the raw tally sheet and automatically store it in the required tables.</p>
<p>No more hassle of sending data to all the departments.</p>
<p>Departments will no longer have to wait for the registrar's office to send the data.</p>
<p>Our automated system ensures error is not introduced by human operators while creating the tally sheet.</p></td>
</tr>
<tr class="even">
<td><strong>Generate dept. revenue and change % chart</strong></td>
<td><p>1. Department Office</p>
<p>2. School</p></td>
<td><p>School must wait for department to finish processing</p>
<p>Time consuming to calculate data and creating charts</p>
<p>Hassle of passing documents from one office to another</p>
<p>Under or overcounting revenue for the current semester</p></td>
<td><p>Schools cannot proceed with other tasks unless they receive this file. If any delay occurs then school has to delay in sending to core analysis.</p>
<p>Lots of data is given in the tally sheet and it takes time to verify, process (e.g., sum up sections etc.).</p>
<p>Error is carries forward from registrar’s tally sheet</p></td>
<td><p>Generating charts automatically from data stored in SEAS will eliminate all of these issues.</p>
<p>Charts will be available to all instantly after the tally sheet is uploaded by admin - no need for manual calculation, compilation and moving documents.</p>
<p>Human error virtually eliminated from the process</p></td>
</tr>
<tr class="odd">
<td><strong>Generate School revenue table and chart</strong></td>
<td><p>1. School</p>
<p>2. Core analysis team</p></td>
<td>Delay in sending the file to the core analysis team.</td>
<td>Delay can occur because the school might have other tasks at hand which delaying them to finish off this work.</td>
<td>The system will automatically generate the chart so School does not have to take time to send it through other mediums. The core analysis team will be able to view whenever they want. So, delays are eliminated</td>
</tr>
<tr class="even">
<td><strong>Generate school class size distribution chart</strong></td>
<td><p>1. School</p>
<p>2. Core analysis team</p></td>
<td><p>School-level processing may be delayed.</p>
<p>School cannot trust Department processing</p></td>
<td><p>Department needs time to manually process the data before sending so a delay might occur in sending the processed data thus school will also have to delay their work.</p>
<p>Manual processing done by the department might introduce scope for operator error. Schools either have to request a corrected version or proceed with incorrect data.</p>
<p>If errors are found which are made by school, then, School might have to redo the whole operation once again which will consume more of their time that could have been spent in doing other pending tasks.</p></td>
<td>Keep data in the system’s database and the system automatically generates charts to view for all users, removing the need for department level processing which highly removes human prone errors made by the department or school.</td>
</tr>
<tr class="odd">
<td><strong>Prepare IUB Revenue Distribution related Charts and Tables</strong></td>
<td>Core Analysis Team</td>
<td><p>Accumulated totals calculations are particularly prone to inaccuracy and hence the final reports often have inaccurate charts and tables.</p>
<p>Storage and handling of Past Revenue Reports data have become time-consuming and difficult.</p></td>
<td><p>Since the calculations are done in spreadsheets, errors are introduced because of using incorrect formulas or performing the calculations on an incorrect selection of dataset because these are manually done.</p>
<p>Over time, storing and retrieving previous reports data in distributed spreadsheet files (separately stored on individual computers) has become increasingly complex due to the incoherent folder structure maintained by the user of those individual computers.</p></td>
<td><p>Calculations can be performed automatically by a system with a database, where the datasets will only need to be uploaded to the system and the system will take care of the rest. Hence, human prone errors are eliminated. Core analysis team can spend more time in analyzing rather than preparing documents.</p>
<p>These issues can be resolved by storing these data tables in a centralized database and providing required departments and offices with access to view, use, and print them via a user interface.</p></td>
</tr>
<tr class="even">
<td><strong>Prepare Resource Related Charts and Tables</strong></td>
<td><p>1. Core analysis team</p>
<p>2. Higher Authority</p></td>
<td><p>Skewed analysis by core analysis team</p>
<p>Higher Authority has to wait for all the processing to be done</p>
<p>Expensive process as more people is involved in completing a few tasks.</p></td>
<td><p>Errors introduced lower in the processing chain can skew their analysis.</p>
<p>Multi-stage process that is slow to get done will have an effect in getting and viewing all the required charts</p>
<p>Lots of people are required to generate a few charts and tables. Thus, higher expenses for IUB to bear.</p></td>
<td><p>Data, if kept in a system’s database, can easily be pulled by our system to do statistical analysis. Moreover, the chances of human prone error gets reduced greatly.</p>
<p>In addition, no delay will occur as charts and tables are generated by the system automatically. Therefore, higher authority can have access to information any time.</p>
<p>The system reduces the number of people required behind the whole process.</p></td>
</tr>
<tr class="odd">
<td><strong>Revise room assignment</strong></td>
<td><p>1. Core Analysis Team</p>
<p>2.Registrar’s Office</p></td>
<td><p>Misallocation of rooms with respect to enrollment.</p>
<p>It takes core analysis team a long time in generating resource usage and requirement data.</p></td>
<td><p>Due to manual process, cannot use data science methods to predict classroom requirements ahead of time so that repeated revisions can be avoided.</p>
<p>Core analysis team can only work on requirement data once schools' hand over their work. Therefore, it is very time consuming.</p></td>
<td>Data, if kept in a database can be, can easily be pulled by our system to create resource and class requirements related charts and tables immediately after the database is updated after student registration so register office does not have to wait for core analysis team. Moreover, registrar office has more time to efficiently allocate rooms to each sections.</td>
</tr>
</tbody>
</table>

##  Rich Picture - Proposed System 

<img src="media/image11.png" style="width:6.01806in;height:6.34292in" alt="Diagram Description automatically generated" />

<span id="_Toc91299070" class="anchor"></span>Figure Rich Picture of
Proposed System

## Six Elements Analysis - Proposed System

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Process</strong></td>
<td colspan="6"><strong>System Roles</strong></td>
</tr>
<tr class="even">
<td><strong>Human</strong></td>
<td><strong>Non-Computing Hardware</strong></td>
<td><strong>Computer Hardware</strong></td>
<td><strong>Software</strong></td>
<td><strong>Database</strong></td>
<td><strong>Network &amp; Communication</strong></td>
</tr>
<tr class="odd">
<td><strong>Prepare Classroom Requirement list for different Sections</strong></td>
<td><p><strong>Department:</strong></p>
<p>1. Logs into SEAS.</p>
<p>2. Views “Revenue Of School” page to check the department growth for chosen semester of their choice.</p>
<p>3. View “Enrollment Information (Compact)” to see number of sections falling in different enrollment groups</p>
<p>4. Views “Classroom Requirement” page for chosen semester of their choice.</p>
<p>5. For more insight the user checks the “Enrollment Information (Expanded)” for chosen semester of their choice.</p>
<p>6. Then user views “Usage of The Resources” page for insight of current IUB resources for chosen semester of their choice.</p>
<p>7. Prepares expected required classrooms list based on the previous semester’s information.</p>
<p>8. Send the classroom allocation files to the registrar's office.</p>
<p><strong>Registrar’s Office:</strong></p>
<p>1. Receives the classroom allocation files from respective departments.</p>
<p>2. Updates classroom allocation in iRAS.</p>
<p>3. Uploads it in “Update Database” page in SEAS.</p>
<p>4. Stores classroom allocation list (Hardcopy and Softcopy) in archive.</p></td>
<td><p><strong>Pen &amp; paper</strong></p>
<p>1. Hard copy of list printed and signed before storing for future reference.</p></td>
<td><p><strong>Computer</strong></p>
<p>1. It is used to create sections, and to send a list to the registrar.</p>
<p><strong>Printer</strong></p>
<p>1.Used to print the hardcopy of the file.</p></td>
<td><p><strong>SEAS:</strong></p>
<p>1. For viewing the different pages required to make predictions</p>
<p><strong>Microsoft Office</strong></p>
<p>1. Microsoft Office will be used to make the document.</p>
<p><strong>Gmail</strong></p>
<p>1. Used to email the files to the registrar.</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Contains historical classroom and section data that the system draws from to show charts and tables.</p>
<p><strong>Department Archive:</strong></p>
<p>Stores the hardcopy/softcopy of previous semester data that is used to make the predictions.</p></td>
<td><p><strong>Internet</strong></p>
<p>For email communication between offices.</p>
<p><strong>Intercom:</strong></p>
<p>For rapid communication between offices</p></td>
</tr>
<tr class="even">
<td><strong>Upload Tally sheet</strong></td>
<td><p><strong>Registrar’s Office:</strong></p>
<p>1. Log in to iRAS</p>
<p>2. Download the semester wise tally sheet.</p>
<p>3. Log in to SEAS.</p>
<p>4. Upload tally sheet in the “Update Database” page in SEAS.</p>
<p>5. Notify the department upon successful addition to the database</p></td>
<td></td>
<td><p><strong>Computer</strong></p>
<p>1. For accessing IRAS and SEAS.</p>
<p>.</p>
<p>2. For emailing the offices informing them of the tally sheet being uploaded to SEAS</p></td>
<td><p><strong>IRAS:</strong></p>
<p>Generates downloadable raw tally sheet as students enroll into courses.</p>
<p><strong>SEAS:</strong></p>
<p>Tally sheet uploaded here</p>
<p><strong>Gmail</strong></p>
<p>Preferred email client to email the departments with</p></td>
<td><p><strong>SEAS</strong></p>
<p><strong>Database:</strong></p>
<p>Stores tally sheet data</p></td>
<td><p><strong>Internet</strong></p>
<p>1. For email communication between offices.</p>
<p>2. To access IRAS and SEAS.</p></td>
</tr>
<tr class="odd">
<td><strong>View all School and department related Revenue tables and charts</strong></td>
<td><p><strong>Higher Authority:</strong></p>
<p>1. Login to SEAS.</p>
<p>2. Select the “Revenue Of School” option.</p>
<p>3. Select the school whose metrics to view e.g., SETS from the combo box and click “load".</p>
<p>4. View revenue Trend of Departments chart.</p>
<p>5. View Revenue Distribution among Departments chart.</p>
<p>6. Revenue and % Change charts of each department is collapsed and can be viewed after clicking a button.</p>
<p>7. Table of Historical Revenue Data And % Change in revenue of each department and an overall % change of previous year of the selected school is also collapsed and can be viewed after clicking a button.</p>
<p>8. User can print the whole page if desired.</p></td>
<td><p><strong>Paper:</strong></p>
<p>1. For charts and table printing</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. Used to access SEAS</p>
<p><strong>Printer:</strong></p>
<p>1. For printing the table and charts</p></td>
<td><p><strong>SEAS:</strong></p>
<p>1. Calculates total revenue of a department by multiplying course credit by number of students enrolled in each of the sections of its courses.</p>
<p>2. Department data added to give total school revenue</p>
<p>3. Percentage change vs. previous semesters calculated for every data point.</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Contains historical enrollment data that SEAS draws from to generate tables and charts</p></td>
<td><p><strong>Internet</strong></p>
<p>For accessing SEAS.</p></td>
</tr>
<tr class="even">
<td><strong>View IUB revenue table and charts</strong></td>
<td><p><strong>Higher Authority:</strong></p>
<p>1. Login to SEAS.</p>
<p>2. Select the “Revenue Of IUB” option.</p>
<p>3. View revenue Trend of Schools chart.</p>
<p>4. View Revenue Distribution among Schools chart.</p>
<p>4. View Revenue and % Change Chart.</p>
<p>5. Table of Historical Revenue Data And % Change in revenue from previous year of the whole of IUB is also collapsed and can be viewed after clicking a button.</p>
<p>6. Print any chart along with the table if desired.</p></td>
<td><p><strong>Paper:</strong></p>
<p>1. For charts and table printing</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. Used to access SEAS</p>
<p><strong>Printer:</strong></p>
<p>1. For printing the table and charts</p></td>
<td><p><strong>SEAS:</strong></p>
<p>1. Calculates total revenue of a department by multiplying course credit by number of students enrolled in each of the sections of its courses.</p>
<p>2. Department data added to give total school revenue</p>
<p>3. Repeat for every school to make the table of revenue.</p>
<p>4. Percentage change vs. previous semesters calculated for every data point.</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Contains historical enrollment data that SEAS draws from to generate table and charts</p></td>
<td><p><strong>Internet</strong></p>
<p>For accessing SEAS.</p></td>
</tr>
<tr class="odd">
<td><strong>View class size distribution data for schools</strong></td>
<td><p><strong>Higher Authority:</strong></p>
<p>1. Logs into SEAS.</p>
<p>2. User clicks on navigation bar.</p>
<p>3. To view enrollment information, user has a choice to view it in expanded or compact form.</p>
<p>4. If enrollment information [Expanded] selected,</p>
<p>a.User selects a semester and a year</p>
<p>b. Views the course distribution table.</p>
<p>5. Else if Enrollment information [compact] chosen then,</p>
<p>a.User has to select a semester and a year of their desire.</p>
<p>b.Views number of sections falling in different enrollment groups table</p>
<p>c. Also views the above table information in a bar chart and line chart.</p>
<p>6. User has a choice to print any of the pages</p></td>
<td><p><strong>Paper:</strong></p>
<p>1. Needed to print if the user wants to.</p></td>
<td><p><strong>Computer/Mobile:</strong></p>
<p>1. Used to access the SEAS.</p>
<p>2. For viewing charts/tables.</p>
<p><strong>Printer:</strong></p>
<p>1. Needed to print if the user wants to (after downloading)</p></td>
<td><p><strong>SEAS:</strong></p>
<p>1. Creates table (Expanded), with columns for each school, that counts the number of sections for each enrollment value. And totals the columns and rows.</p>
<p>2. Creates the same table (Compact) but groups the enrollment into specific categories.</p>
<p>3. Creates a Bar Chart for each enrollment category for each school. Also, adds a line of totals for each category. All from the created compact table</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Contains historical enrollment data that SEAS draws from to show charts and tables.</p></td>
<td><p><strong>Internet</strong></p>
<p>For accessing the SEAS.</p></td>
</tr>
<tr class="even">
<td><strong>Views resource requirement and usage data</strong></td>
<td><p><strong>Higher Authority:</strong></p>
<p>1. Log in to SEAS.</p>
<p>2. Select “Usage Of The Resources” page.</p>
<p>3. Select the current semester and year.</p>
<p>4. Views Usage Of the Resources table</p>
<p>5. Views IUB Available Resources Table</p>
<p>6. Select “Availability and course offering comparison” option</p>
<p>7. Select the current semester and year.</p>
<p>8. View “Comparison of IUB resources” table.</p>
<p>9. View Resource Usage Comparison bar chart.</p></td>
<td><p><strong>Paper:</strong></p>
<p>1. Needed to print if the user wants to.</p></td>
<td><p><strong>Computer/Mobile:</strong></p>
<p>1. Used to access the SEAS.</p>
<p><strong>Printer:</strong></p>
<p>1. Needed to print if the user wants to.</p></td>
<td><p><strong>SEAS</strong></p>
<p>1. Creates a table that has Sums of enrollment for each school for the semester.</p>
<p>2. Averages the Sum over the number of sections provided by the school.</p>
<p>3.Averages the room capacity of all the rooms used by each school.</p>
<p>4. Compares the columns created in step 2 and 3 and calculates the Difference for each school.</p>
<p>5. Calculates the % Unused by using the formula: Difference/AvgRoom*100 for each school</p>
<p>6. Retrieves IUB available number of rooms for different class sizes from database and calculates Capacity by multiplying Class size and number of rooms.</p>
<p>7. Total Capacity for 6 slot and 7 slot semester is calculated by multiplying total capacity of rooms with 12 and 14 respectively.</p>
<p>8. Capacity considering 3.5 course load is calculated by dividing step 7 values by 3.5.</p>
<p>9. Calculates capacity utilization for the semester considering unused % by using the formula [(100-unused percentage)/100*(capacity considering course load)]</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Contains historical enrollment and IUB’s existing resource capacity data that the system draws from to show charts and tables.</p></td>
<td><p><strong>Internet</strong></p>
<p>For accessing the SEAS.</p></td>
</tr>
<tr class="odd">
<td><strong>Revise Room Assignment </strong></td>
<td><p><strong>Registrar’s Office:</strong> </p>
<p>1. Log in to SEAS.</p>
<p>2. Select “Availability and course offering comparison” option</p>
<p>3. Select the current semester and year.</p>
<p>4. View “Comparison of IUB resources” table.</p>
<p>5. View Resource Usage Comparison bar chart at the same time.</p>
<p>4. After viewing charts, revise the room assignment based on surplus and deficit if required.</p>
<p>5. Select “Administration” page.</p>
<p>6. Select “Section ts”</p>
<p>7. Change the classroom allocation for desired section.</p>
<p>8. Reflect the same changes in iRAS</p>
<p>9. Notify the departments about the revised room assignment.</p>
<p>10. Archive the files (Hardcopy and Softcopy)</p></td>
<td><p><strong>Paper:</strong></p>
<p>Needed for printing the hardcopy for archiving.</p></td>
<td><p><strong>Computer:</strong></p>
<p>1. Used to access SEAS.</p>
<p>2. Used to access email clients to notify department.</p>
<p><strong>Printer:</strong></p>
<p>To print the hardcopy of the revised data.</p></td>
<td><p><strong>SEAS:</strong></p>
<p>1. For viewing the “Availability and course offering comparison” charts and bar chart.</p>
<p><strong>Microsoft Office</strong></p>
<p>1. Microsoft Office will be used to update classroom allocation sheet.</p>
<p>2. To view the revised tally sheet.</p>
<p><strong>Gmail</strong></p>
<p>1. Used to email the files to the registrar.</p></td>
<td><p><strong>SEAS Database:</strong></p>
<p>1. Enrollment data of the current semester is updated from the new tally sheet.</p>
<p><strong>Archive:</strong></p>
<p>1.Stores revised section enrollment data.</p>
<p> </p></td>
<td><p><strong>Internet:</strong></p>
<p>1.For email communication between offices.</p>
<p>2. For accessing SEAS and iRAS</p>
<p><strong>Intercom:</strong></p>
<p>For rapid communication between offices</p></td>
</tr>
</tbody>
</table>

## BUsiness Process Model and Notation 2.0 – Proposed System

<img src="media/image12.png" style="width:6.59094in;height:6.74386in" />

<span id="_Toc91299071" class="anchor"></span>Figure Prepare Classroom
Requirement list for different Sections

<img src="media/image13.png" style="width:6.57547in;height:2.73578in" />

<span id="_Toc91299072" class="anchor"></span>Figure Upload Tally Sheet

<img src="media/image14.png" style="width:6.59301in;height:4.05033in" />

<span id="_Toc91299073" class="anchor"></span>Figure View all School and
department related Revenue tables and charts.

<img src="media/image15.png" style="width:6.62035in;height:3.66115in" />

<span id="_Toc91299074" class="anchor"></span>Figure View IUB revenue
table and charts.

<img src="media/image16.png" style="width:6.60011in;height:4.9279in" />

<span id="_Toc91299075" class="anchor"></span>Figure View class size
distribution data for schools

<img src="media/image17.png" style="width:6.60377in;height:5.06604in" />

<span id="_Toc91299076" class="anchor"></span>Figure View resource
requirement and usage data

<img src="media/image18.png" style="width:6.54465in;height:4.15858in" />

<span id="_Toc91299077" class="anchor"></span>Figure Revise Room
Assignment

# Chapter 3: Logical System design

##  Business Rules

1.  Academics of IUB are conducted through schools. **SCHOOL** has
    <u>schoolID</u> and <u>schoolName</u>.

2.  A school can have one or many departments. A department must belong
    to one school only. **DEPARTMENT** has <u>departmentID</u>,
    <u>departmentName</u> and  <u>schoolID</u>.

3.  Courses are offered by departments. A department can offer one or
    many courses. A course can be offered under many departments as
    co-offering. **COURSE** has <u>courseID</u>,
    <u>{coOffCourseCode}</u>,  <u>courseName</u>, <u>creditHour</u>, and
    <u>departmentID</u>.

4.  A department may hand over responsibility of offering a course to a
    different department – i.e. a course may change “owners” over the
    years.

5.  Courses are taught by faculties. A faculty can teach many courses.
    **FACULTY** has <u>facultyID</u> and <u>facultyName</u>.

6.  A faculty teaches a section in a classroom. IUB has many classrooms,
    each of which has a fixed maximum capacity. **CLASSROOM** has
    <u>roomID</u> and <u>roomCapacity</u>.

7.  IUB runs its academics through a tri-semester system. Semester can
    be identified by a combination of session and year.

8.  Sections of each course are offered every semester that are taught
    by faculties in assigned classrooms.

9.  Many sections of the same course can be offered in a given semester
    and a faculty can teach more than one section. **SECTION** has
    <u>courseID</u>, <u>semester (session, year)</u>, <u>sectionNum</u>,
    <u>facultyID</u>, <u>roomID</u>, <u>sectionCapacity</u>,
    <u>enrolled</u>, <u>{freeSpace}</u>, <u>{totalStudentCredits}</u>,
    <u>{blockedStudentCredits}</u>, <u>blockedStatus</u> and
    <u>timing(startTime, EndTime, days)</u>.

10. An offered section in a particular semester is identified by
    sectionID, courseID and semester.

11. Classrooms are assigned to sections based on the enrolled class size
    requirement.

12. Classrooms are used in slots. In a particular workday at IUB, a
    classroom can offer 6 or 7 slots.

13. A section can be assigned to only one slot at a time and a
    particular section requires 2 slots per work week.

##  ERD

<img src="media/image19.png" style="width:6.25346in;height:5.30526in" alt="Diagram Description automatically generated" />

<span id="_Toc91299078" class="anchor"></span>Figure 18 ERD

## <img src="media/image20.png" style="width:8.23819in;height:3.27361in" /> Relational Schema

<span id="_Toc91299079" class="anchor"></span>Figure 19 Relational
Schema

##  Normalization

**<u>FUNCTIONAL DEPENDENCIES</u>**

1.  cSchool_ID → cSchoolName

2.  cDepartment_ID → cDepartmentName, cSchool_ID

3.  cCourse_ID → cCourseName, nCreditHour

4.  cCourse_ID, cDepartment_ID, eSession, dYear, nSectionNum →
    cFaculty_ID, cRoom_ID, nSectionCapacity, nEnrolled, bIsBlocked,
    tStartTime, tEndTime, eDays

5.  cCoffCode_ID → cCourse_ID

6.  cRoom_ID → nRoomCapacity

7.  cFaculty_ID → cFacultyName

8.  nCapacity → nRooms

<img src="media/image21.png" style="width:8.19653in;height:6.83819in" />

##  DATA DICTIONARY

School_T

| Name        | Data type | Size | Remark                                                                   |
|-------------|-----------|------|--------------------------------------------------------------------------|
| cSchool_ID  | CHAR      | 5    | Primary key e.g. “SLASS”                                                 |
| cSchoolName | VARCHAR   | 50   | Full name of the school e.g. “School of Liberal Arts and Social Science” |

Department_T

| Name            | Data type | Size | Remark                                                              |
|-----------------|-----------|------|---------------------------------------------------------------------|
| cDepartment_ID  | CHAR      | 5    | Primary key e.g. “EEE”                                              |
| cDepartmentName | VARCHAR   | 50   | Name of the department e.g. “Electrical and Electronic Engineering” |
| cSchool_ID      | CHAR      | 5    | Foreign key from School_T e.g. “SETS”                               |

Course_T

| Name         | Data type | Size | Remark                                        |
|--------------|-----------|------|-----------------------------------------------|
| cCourse_ID   | CHAR      | 7    | Primary key e.g. “CSE303”                     |
| cCourseName  | VARCHAR   | 50   | Name of the course e.g. “Database Management” |
| nCreditHours | TINYINT   |      | Number of credit hours earned in this course  |

CoOfferedCourse_T

| Name         | Data type | Size | Remark                                                                                                    |
|--------------|-----------|------|-----------------------------------------------------------------------------------------------------------|
| cCoffCode_ID | CHAR      | 7    | Primary key e.g. “CSC401”. A course may be co-offered under multiple other codes depending on the program |
| cCourse_ID   | CHAR      | 7    | Foreign key from Course_T e.g. “CSE303”                                                                   |

Faculty_T

| Name         | Data type | Size | Remark                                                                                    |
|--------------|-----------|------|-------------------------------------------------------------------------------------------|
| cFaculty_ID  | CHAR      | 4    | Primary key e.g. “4025”. This is the university-assigned ID number of the faculty member. |
| cFacultyName | VARCHAR   | 50   | Name of the faculty member                                                                |

Classroom_T

| Name          | Data type | Size | Remark                                                                                         |
|---------------|-----------|------|------------------------------------------------------------------------------------------------|
| cRoom_ID      | CHAR      | 10   | Primary key e.g. “BC10015-S". This room number is assigned by the university to all classrooms |
| nRoomCapacity | INT       |      | Maximum number of students the room can hold                                                   |

Section_T

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 58%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Data type</th>
<th>Size</th>
<th>Remark</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>section_ID</td>
<td>BIGINT</td>
<td></td>
<td colspan="2">Auto-generated PK for sections.</td>
</tr>
<tr class="even">
<td>cCoffCode_ID</td>
<td>CHAR</td>
<td>7</td>
<td>Foreign key from CoOfferedCourse_T. Denotes which course this section is of  e.g. “CSC401L”</td>
<td></td>
</tr>
<tr class="odd">
<td>cDepartment_ID</td>
<td>CHAR</td>
<td>5</td>
<td colspan="2">Foreign key from Department_T e.g. “CSE”</td>
</tr>
<tr class="even">
<td>eSession</td>
<td>ENUM</td>
<td></td>
<td><p>Partial Identifier? </p>
<p>Session of the year e.g. Summer, Autumn, Spring</p></td>
<td></td>
</tr>
<tr class="odd">
<td>dYear</td>
<td>YEAR</td>
<td></td>
<td><p>Partial Identifier?</p>
<p>The year this section has been offered in</p></td>
<td></td>
</tr>
<tr class="even">
<td>nSectionNumber</td>
<td>INT</td>
<td></td>
<td><p>Partial Identifier?</p>
<p>Section number e.g. 1</p></td>
<td></td>
</tr>
<tr class="odd">
<td>cFaculty_ID</td>
<td>CHAR</td>
<td>4</td>
<td>Foreign key from Faculty_T e.g. “4025”</td>
<td></td>
</tr>
<tr class="even">
<td>cRoom_ID</td>
<td>CHAR</td>
<td>10</td>
<td>Foreign key from Room_T e.g. “BC10015-S"</td>
<td></td>
</tr>
<tr class="odd">
<td>nSectionCapacity</td>
<td>INT</td>
<td></td>
<td>Maximum number of students allowed to enroll in this section</td>
<td></td>
</tr>
<tr class="even">
<td>nEnrolled</td>
<td>INT</td>
<td></td>
<td>Total number of students enrolled in this section</td>
<td></td>
</tr>
<tr class="odd">
<td>bIsBlocked</td>
<td>BOOLEAN</td>
<td></td>
<td>If blocked, cannot enroll in this section</td>
<td></td>
</tr>
<tr class="even">
<td>tStartTime</td>
<td>TIME</td>
<td></td>
<td>Class starts at e.g. 14:00:00 hours</td>
<td></td>
</tr>
<tr class="odd">
<td>tEndTime</td>
<td>TIME</td>
<td></td>
<td>Class ends at e.g. 15:30:00 hours</td>
<td></td>
</tr>
<tr class="even">
<td>eDays</td>
<td>ENUM</td>
<td></td>
<td>Days of the week that the classes take place on e.g., 'ST','MW','S','M','T','W','R','F','A','AR','TR','MWA','STR','AMW','SMW'</td>
<td></td>
</tr>
</tbody>
</table>

Resource_T

| Name      | Data type | Size | Remark                                                                            |
|-----------|-----------|------|-----------------------------------------------------------------------------------|
| nCapacity | INT       |      | Primary key e.g., 50. This is the capacity of classroom e.g., a 50-capacity class |
| nRoom     | INT       |      | Number of available classrooms in IUB of that size                                |

# Chapter 4: Physical System Design

##  Input Forms 

# 

<img src="media/image22.png" style="width:6.01806in;height:3.38542in" alt="Diagram Description automatically generated with low confidence" />

<img src="media/image23.png" style="width:3.05172in;height:2.39889in" alt="Graphical user interface, application, table Description automatically generated" /><img src="media/image24.png" style="width:4.42258in;height:7.16379in" alt="Graphical user interface, text Description automatically generated" />

##  Output Query & Reports

1.  FUNCTIONALITY-1

<img src="media/image25.png" style="width:6.50903in;height:5.12847in" />

<img src="media/image26.png" style="width:7.14722in;height:8.53403in" />

2.  <img src="media/image27.png" style="width:7.20625in;height:6.04028in" />FUNCTIONALITY-2

<img src="media/image28.png" style="width:4.24097in;height:4.05486in" /><img src="media/image29.png" style="width:6.91319in;height:7.62847in" />

3.  FUNCTIONALITY-3.4

<img src="media/image30.png" style="width:5.87931in;height:5.57879in" alt="Graphical user interface, table Description automatically generated" />

<img src="media/image31.png" style="width:6.64631in;height:6.18937in" />

<img src="media/image32.png" style="width:5.99138in;height:6.22481in" alt="Graphical user interface, text, application Description automatically generated" />

4.  <img src="media/image33.png" style="width:6.45625in;height:5.80764in" />FUNCTIONALITY-5

<img src="media/image34.png" style="width:5.77471in;height:8.82759in" alt="A picture containing diagram Description automatically generated" />

5.  

6.  

7.  <img src="media/image35.png" style="width:6.1375in;height:4.98958in" />FUNCTIONALITY-6

<img src="media/image36.png" style="width:5.7931in;height:9.29996in" />

1.  FUNCTIONALITY-7

<img src="media/image37.png" style="width:5.93103in;height:3.12025in" alt="Graphical user interface, chart Description automatically generated" />

<img src="media/image38.png" style="width:5.93966in;height:2.81495in" alt="Histogram Description automatically generated" />

<img src="media/image39.png" style="width:5.82759in;height:2.7in" alt="Chart, histogram Description automatically generated" />

<img src="media/image40.png" style="width:5.91379in;height:4.49186in" alt="Table Description automatically generated" />

<img src="media/image41.png" style="width:5.86487in;height:8.08947in" />

8.  FUNCTIONALITY-8

<img src="media/image42.png" style="width:5.95283in;height:2.72722in" alt="Graphical user interface, chart Description automatically generated" />

<img src="media/image43.png" style="width:5.98113in;height:2.82037in" alt="Chart, histogram Description automatically generated" />

<img src="media/image44.png" style="width:5.91379in;height:2.67305in" alt="Chart, histogram Description automatically generated" />

<img src="media/image45.png" style="width:6.01806in;height:2.79868in" alt="Graphical user interface, chart Description automatically generated" />

<img src="media/image46.png" style="width:5.94047in;height:2.75542in" alt="Chart, histogram Description automatically generated" />

<img src="media/image47.png" style="width:5.89655in;height:4.67956in" alt="Table Description automatically generated" /><img src="media/image48.png" style="width:6.08621in;height:8.39477in" />

# CHAPTER 5: Conclusion

## Problems and solution

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROBLEMS</th>
<th>SOLUTIONS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Dataset file had numerous issues that are not suitable for relational database paradigm such as:</p>
<p>Column headers varied across files</p>
<p>Blocked columns had very weird values like B-0 B-1 B- which needlessly convoluted.</p>
<p>Faculty name and id were combined</p></td>
<td><p>The following solutions were implemented to solve this problem:</p>
<p>Had to manually fix each value.</p>
<p>Used regular expressions to change values to either 1 or 0.</p>
<p>Pandas were used to separate it into each separate column of ID and Name.</p></td>
</tr>
<tr class="even">
<td>Population SQL query script did not work properly for windows users which meant loads of missing data.</td>
<td>The line terminators for Windows and Unix are different, so we modified the script to take that into account.</td>
</tr>
<tr class="odd">
<td>Some courses had changed departments throughout IUB history such as HEA used to belong to a SLASS dept. then it shifted into an SPPH dept which meant that a course cannot reliably determine a department.</td>
<td>We included the department column in the section table and made sure that course code and dept. id were unique together.</td>
</tr>
<tr class="even">
<td>Our overall mindset was to let MySQL do most of the heavy lifting when it came to generating tables however, it meant very huge and repeated queries. Thus, it was becoming more complicated.</td>
<td>To overcome this issue, we had to utilize LAG, dynamic SQL, CASE statements into the queries for some cases.</td>
</tr>
<tr class="odd">
<td>We thought we had to extrapolate the number of rooms IUB had available from the section data - this obviously is not accurate since IUB's available resources are always subject to change (building shifts discontinuing classrooms for example).</td>
<td>We created a separate Resources Table in the Database that has hardcoded values that the Admin can change whenever IUB decides to renovate the rooms.</td>
</tr>
</tbody>
</table>

| PROBLEMS                                                                                                                                                                            | UNSOLVED                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schools except SETS do not have distinguished Department names in the department column of the tally sheets so, we could not show School Revenue Breakdown pages for other Schools. | It is a dataset issue which is out of our hands; however, our system is capable of showing the breakdown of other schools only if the dataset is corrected. |

## B. Additional feature and future development

1.  Currently, the user must update the database manually by uploading
    the tally sheet after every registration therefore if we connect
    IRAS database with our SEAS database then even this manual work can
    be eliminated.

2.  Currently, every time a user refreshes the website or clicks load,
    the same queries are run on the database. We can make it more
    efficient if we implement cache features in our website.

3.  At this moment, users see all of the revenue data from the inception
    of IUB to the current time. We can implement a feature where they
    can have a choice in choosing to view a certain range of
    years/semesters of revenue data.

4.  Given our dataset we can get more interesting insights into the
    state of IUB such as the total working hours/classes of number of
    each faculty in a week. Or, similar to Enrollment table\[expanded\],
    how many faculties from each School/dept take a specific number of
    courses.

5.  We can also partially infer faculty popularity among students by
    calculating average enrollment in each of their sections throughout
    their tenure.

6.  A more sophisticated system can be made which will generate the
    number of required sections for each course for a new semester by
    collecting and analyzing previous enrollment data of each course.

# References

| \[1\] | IUB, "Independent University, Bangladesh," \[Online\]. Available: http://www.iub.edu.bd/. \[Accessed 2021\].   |
|-------|----------------------------------------------------------------------------------------------------------------|
| \[2\] | J. K. T. A. A. M. T. S. A. Sadia Khan, "SPM," Group 1, Autumn 2020, Dhaka, 2020.                               |
| \[3\] | T. S. H. A. M. A. M. M. M. R. R. H. Udipto Mazumdar, "SPMS 2.0," Group 1, Section 1, Spring 2021, Dhaka, 2021. |
