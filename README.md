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

