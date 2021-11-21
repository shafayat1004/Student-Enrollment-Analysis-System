from django.db import models

# Create your models here.

class FixedCharField(models.CharField):
    def db_type(self, connection):
        varchar: str = super().db_type(connection)
        char: str = varchar.replace('varchar', 'char')
        return char

class YearField( models.Field ):
    def db_type( self, connection ):
        return 'YEAR'

class TimeField( models.Field ):
    def db_type( self, connection ):
        return 'TIME'

class School ( models.Model ):
    cSchool_ID = FixedCharField(max_length = 5, primary_key = True)
    cSchoolName = models.CharField(max_length = 50)

class Department ( models.Model ):
    cDepartment_ID = models.FixedCharField( max_length = 3, primary_key = True )
    cDepartmentName = models.CharField( max_length = 50 )
    cSchool_ID = models.ForeignKey( School, on_delete = models.CASCADE )

class Course ( models.Model ):
    cCourse_ID = models.FixedCharField( max_length = 7, primary_key = True )
    cCourseName = models.CharField( max_length = 50 )
    nCreditHours = models.PositiveSmallIntegerField( max_length = 50 )
    cDepartment_ID = models.ForeignKey( Department, on_delete = models.CASCADE )

class Faculty ( models.Model ):
    cFaculty_ID = models.FixedCharField( max_length = 4, primary_key = True )
    cFacultyName = models.CharField( max_length = 50 )
