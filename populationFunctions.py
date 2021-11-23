from pathlib import Path
from pandas import read_excel, read_csv
from re import compile
from numpy import nan

def csvToMySQL(csvPath, csvColumns, tableName, tableColumns, local=True): #TODO might have to set this to false for the actual app
    csv_variables = ''

    firstRow = read_csv(csvPath, nrows=1, sep='\t')
    for i in firstRow:
        if i in csvColumns:
            if csv_variables=='':
                csv_variables+='(@' + i
            else:
                csv_variables+=',@' + i
        else:
            if csv_variables=='':
                csv_variables+='(@d'
            else:
                csv_variables+=',@d'
    csv_variables+=')'


    tableAssignments = ''
    for i in range(len(tableColumns)):
        if tableAssignments == '':
            tableAssignments+=tableColumns[i] + '=@' + csvColumns[i]
        else:
            tableAssignments+=',' + tableColumns[i] + '=@' + csvColumns[i]

    colNotInCSVComment = '\n-- If any @variable in SET is not in above line, query wont work. Needs optimization'

    sqlQuery = 'LOAD DATA '
    if local is True:
        sqlQuery+= 'LOCAL'

    sqlQuery+='\nINFILE "' + str(csvPath) + '" \nINTO TABLE ' + tableName + ' \nFIELDS TERMINATED BY "\\t"\nIGNORE 1 LINES \n' + csv_variables + colNotInCSVComment + ' \nSET ' + tableAssignments + ';'
    
    return sqlQuery

def xlsxToMySQL(xlsxPath, xlsxColumns, tableName, tableColumns):
    if len(xlsxColumns)!= len(tableColumns):
        return
    read_file = read_excel (xlsxPath)
    csvSavePath = Path.joinpath(xlsxPath.parent, xlsxPath.stem + '.csv')
    read_file.to_csv (csvSavePath, index = None, header=True, columns=xlsxColumns, sep='\t')
    return csvToMySQL(csvSavePath, xlsxColumns, tableName, tableColumns)

def fillClassroom_T(csvPath):
    table = 'Classroom_T'
    csvColumns = ['ROOM_ID', 'ROOM_CAPACITY']
    tableColumns = ['cRoom_ID', 'nRoomCapacity']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillFaculty_T(csvPath):
    table = 'Faculty_T'
    # TODO need to separate FACULTY ID and NAME

    csvColumns = ['FACULTY_ID', 'FACULTY_NAME']
    tableColumns = ['cFaculty_ID', 'cFacultyName']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillSchool_T(csvPath):
    table = 'School_T'
    #TODO  There is no such thing as schoolname in any dataset

    csvColumns = ['SCHOOL_TITLE', 'SCHOOL_NAME']
    tableColumns = ['cSchool_ID', 'cSchoolName']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillDepartment_T(csvPath):
    #TODO  There is no such thing as department id in classsize dataset

    table = 'Department_T'
    csvColumns = ['DEPARTMENT_ID', 'DEPARTMENT_NAME', 'SCHOOL_TITLE']
    tableColumns = ['cDepartment_ID', 'cDepartmentName', 'cSchool_ID']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillCourse_T(csvPath):
    table = 'Course_T'
    csvColumns = ['COFFER_COURSE_ID', 'COURSE_NAME', 'CREDIT_HOUR', 'DEPARTMENT_ID']
    tableColumns = ['cCourse_ID', 'cCourseName', 'nCreditHours', 'cDepartment_ID'] 
    #TODO  There is no such thing as department id in classsize dataset so omitted mentioning 'cDepartment_ID'] 
    
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillCoOfferedCourse_T(csvPath):
    table = 'CoOfferedCourse_T'
    csvColumns = ['COFFERED_WITH', 'COFFER_COURSE_ID']
    # TODO need to separate multivalued COFFERED_WITH ids

    tableColumns = ['cCoffCode_ID', 'cCourse_ID']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def fillSection_T(csvPath):
    table = 'Section_T'
    csvColumns = ['Semester', 'ST_MW', 'Year', 'SECTION', 'CAPACITY', 'ENROLLED', 'BLOCKED', 'START_TIME', 'END_TIME', 'COFFER_COURSE_ID', 'FACULTY_ID', 'ROOM_ID'] 
    #Took liberty here with start time. In dataset it's STRAT_TIME 
    # TODO need to separate FACULTY ID and NAME

    tableColumns = ['eSession', 'eDays', 'dYear', 'nSectionNumber', 'nSectionCapacity', 'nEnrolled', 'bIsBlocked', 'tStartTime', 'tEndTime', 'cCoffCode_ID', 'cFaculty_ID', 'cRoom_ID']
    return '-- Populating ' + table + '\n' + csvToMySQL(csvPath, csvColumns, table, tableColumns) + '\n\n\n'

def xlsxToCSV(xlsxPath):
    read_file = read_excel (xlsxPath)
    csvSavePath = Path.joinpath(xlsxPath.parent, xlsxPath.stem + '.csv')
    read_file.to_csv (csvSavePath, sep='\t', index = None, header=True)
    return csvSavePath

def populateAllTables(csvPath):

    return '-- AUTO-GENERATED QUERY FROM populateALLTables FUNCTION\n\n\n' + fillClassroom_T(csvPath) + fillFaculty_T(csvPath) + fillSchool_T(csvPath) + fillDepartment_T(csvPath) + fillCourse_T(csvPath) + fillCoOfferedCourse_T(csvPath) + fillSection_T(csvPath)


def optimiseXLSX(xlsxPath):
    csvPath = xlsxToCSV(xlsxPath)
    dataset = read_csv(csvPath, sep='\t')
    dataset.dropna(inplace=True)

    # Separating faculty id and name
    facultyDataFrame = dataset['FACULTY_FULL_NAME'].str.split("-", n = 1, expand = True)

    # TODO for some reason the code didn't work for the larger xlsx file.
    # print(facultyDataFrame[0])
    dataset['FACULTY_ID'] = facultyDataFrame[0]
    dataset['FACULTY_NAME'] = facultyDataFrame[1] 
    dataset.drop(columns =["FACULTY_FULL_NAME"], inplace = True)


    #Creating SCHOOL_NAME Column
    schoolNameDict = {
        'SBE'   : 'School of Business',
        'SLASS' : 'School of Liberal Arts and Social Sciences',
        'SETS'  : 'School of Engineering, Technology and Sciences',
        'SPPH'  : 'School of Pharmacy and Public Health',
        'SELS'  : 'School of Environment and Life Sciences'
    }
    dataset['SCHOOL_NAME'] = dataset['SCHOOL_TITLE'].replace(schoolNameDict)

    #Creating DEPT_ID Column
    courseToDepDict = {
        r'^CCR....?$' : 'CSE',
        r'^ETE....?$' : 'EEE',
        r'^PHY....?$' : 'PS',
        r'^ECR....?$' : 'EEE',
        r'^CNC....?$' : 'CSE',
        r'^CEN....?$' : 'CSE',
        r'^SEN....?$' : 'CSE',
        r'^CIS....?$' : 'CSE',
        r'^CSC....?$' : 'CSE',
        r'^CSE....?$' : 'CSE',
        r'^EEE....?$' : 'EEE',
        r'^MAT....?$' : 'PS',
        r'^TCL....?$' : 'PS',
        r'.......?$'  : nan
    }
    dataset['DEPARTMENT_ID'] = dataset['COFFER_COURSE_ID'].replace(regex=courseToDepDict)

    #Creating DEPARTMENT_NAME Column
    depNameDict = {
        'CSE'  : 'Department of Computer Science and Engineering',
        'PS'   : 'Department of Physical Sciences',
        'EEE'  : 'Department of Electrical and Electronic Engineering'
    }
    dataset['DEPARTMENT_NAME'] = dataset['DEPARTMENT_ID'].replace(depNameDict)


    #Optimizing BLOCKED Column
    blockDict = {
        r'^B..?$' : 1,
        r'..?$'   : 0
    }
    dataset['BLOCKED'] = dataset['BLOCKED'].replace(regex=blockDict)


    dataset.to_csv(csvPath, sep='\t',index = None, header=True)
    return csvPath





xlsxPath1 = Path('/home/shafayat/Coding/django/2021 Summer and Spring.xlsx')
xlsxPath2 = Path('/home/shafayat/Coding/django/2009 Spring to 2021 Summer.xlsx')

output1 = populateAllTables(optimiseXLSX(xlsxPath1))
with open("PopulateDatabase2021.sql", "w") as text_file:
    text_file.write(output1)
    print('Output 1 complete')

# output2 = populateAllTables(optimiseXLSX(xlsxPath2))
# with open("PopulateDatabasePre2021.sql", "w") as text_file:
#     text_file.write(output2)
#     print('Output 2 complete')


