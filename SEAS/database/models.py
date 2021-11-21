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
    cDepartment_ID = FixedCharField( max_length = 3, primary_key = True )
    cDepartmentName = models.CharField( max_length = 50 )
    cSchool_ID = models.ForeignKey( School, on_delete = models.CASCADE )

class Course ( models.Model ):
    cCourse_ID = FixedCharField( max_length = 7, primary_key = True )
    cCourseName = models.CharField( max_length = 50 )
    nCreditHours = models.PositiveSmallIntegerField()
    cDepartment_ID = models.ForeignKey( Department, on_delete = models.CASCADE )

class Faculty ( models.Model ):
    cFaculty_ID = FixedCharField( max_length = 4, primary_key = True )
    cFacultyName = models.CharField( max_length = 50 )
    
class Classroom ( models.Model ):
    cRoom_ID = FixedCharField( max_length = 10, primary_key= True )
    nRoomCapacity = models.PositiveSmallIntegerField()


class CoOfferedCourse ( models.Model ):
    cCoffCode_ID = FixedCharField( max_length = 7, primary_key = True )
    cCourse_ID =  models.ForeignKey( Course , on_delete = models.CASCADE )
    

class Section ( models.Model ): 
    # TODO need to figure out FK as PK/Composite keys
    cCoffCode_ID = models.ForeignKey( CoOfferedCourse , on_delete = models.CASCADE )
    dYear = YearField()
    nSectionNumber = models.IntegerField()
    cFaculty_ID = models.ForeignKey( Faculty , on_delete = models.CASCADE )
    cRoom_ID = models.ForeignKey( Classroom , on_delete = models.CASCADE )
    nSectionCapacity = models.PositiveSmallIntegerField()
    nEnrolled = models.PositiveSmallIntegerField()
    bIsBlocked = models.BooleanField()
    tStartTime = TimeField()
    tEndTime = TimeField()
    # eDays 
    # eSession
