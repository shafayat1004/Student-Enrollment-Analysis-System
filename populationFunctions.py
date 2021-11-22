import csv
from pathlib import Path
from pandas import read_excel, read_csv

def csvToMySQL(csvPath, csvColumns, tableName, tableColumns):
    csv_variables = ''

    firstRow = read_csv(csvPath, nrows=1)
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


    sqlQuery = 'LOAD DATA \nINFILE "' + str(csvPath) + '" \nINTO TABLE ' + tableName + ' \nFIELDS TERMINATED BY ","\nIGNORE 1 LINES \n' + csv_variables + ' \nSET ' + tableAssignments + ';'
    
    return sqlQuery

def xlsxToMySQL(xlsxPath, xlsxColumns, tableName, tableColumns):
    if len(xlsxColumns)!= len(tableColumns):
        return
    read_file = read_excel (xlsxPath)
    csvSavePath = Path.joinpath(xlsxPath.parent, xlsxPath.stem + '.csv')
    read_file.to_csv (csvSavePath, index = None, header=True, columns=xlsxColumns)
    return csvToMySQL(csvSavePath, xlsxColumns, tableName, tableColumns)


xlsxPath = Path('/home/shafayat/Coding/django/2021 Summer and Spring original.xlsx')
xlsxColumns = ['ROOM_ID', 'ROOM_CAPACITY']
tableColumns = ['cRoom_ID', 'nRoomCapacity']
tableName = 'TESTSite_Database.Classroom_T'

print(xlsxToMySQL(xlsxPath, xlsxColumns, tableName, tableColumns))