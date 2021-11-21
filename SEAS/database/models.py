from django.db import models
from django_mysql.models import EnumField


class FixedCharField(models.CharField):
    def db_type(self, connection):
        varchar: str = super().db_type(connection)
        char: str = varchar.replace('varchar', 'char')
        return char

class YearField( models.Field ):
    def db_type( self, connection ):
        return 'YEAR'

class TimeField( models.CharField ):
    def db_type(self, connection):
        varchar: str = super().db_type(connection)
        time: str = varchar.replace('varchar', 'time')
        return time

class ClassroomT(models.Model):
    cRoom_ID = FixedCharField(db_column='cRoom_ID', primary_key=True, max_length=10)
    nRoomCapacity = models.IntegerField(db_column='nRoomCapacity', blank=True, null=True)

    class Meta:
        db_table = 'Classroom_T'


class CoofferedcourseT(models.Model):
    cCoffCode_ID = FixedCharField(db_column='cCoffCode_ID', primary_key=True, max_length=7)
    cCourse_ID = models.ForeignKey('CourseT', models.DO_NOTHING, db_column='cCourse_ID', blank=True, null=True)

    class Meta:
        db_table = 'CoOfferedCourse_T'


class CourseT(models.Model):
    cCourse_ID = FixedCharField(db_column='cCourse_ID', primary_key=True, max_length=7)
    cCourseName = models.CharField(db_column='cCourseName', max_length=30, blank=True, null=True)
    nCreditHours = models.IntegerField(db_column='nCreditHours', blank=True, null=True)
    cDepartment_ID = models.ForeignKey('DepartmentT', models.DO_NOTHING, db_column='cDepartment_ID', blank=True, null=True)

    class Meta:
        db_table = 'Course_T'


class DepartmentT(models.Model):
    cDepartment_ID = FixedCharField(db_column='cDepartment_ID', primary_key=True, max_length=3)
    cDepartmentName = models.CharField(db_column='cDepartmentName', max_length=50, blank=True, null=True)
    cSchool_ID = models.ForeignKey('SchoolT', models.DO_NOTHING, db_column='cSchool_ID', blank=True, null=True)

    class Meta:
        db_table = 'Department_T'


class FacultyT(models.Model):
    cFaculty_ID = FixedCharField(db_column='cFaculty_ID', max_length=4, primary_key=True)
    cFacultyName = models.CharField(db_column='cFacultyName', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Faculty_T'


class SchoolT(models.Model):
    cSchool_ID = FixedCharField(db_column='cSchool_ID', primary_key=True, max_length=5)
    cSchoolName = models.CharField(db_column='cSchoolName', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'School_T'


class SectionT(models.Model):
    section_id = models.BigAutoField(db_column='section_ID', primary_key=True)
    
    cCoffCode_ID = models.OneToOneField(CoofferedcourseT, models.DO_NOTHING, db_column='cCoffCode_ID')
    
    eSession = EnumField(choices=['Autumn', 'Summer', 'Spring'], db_column='eSession')
    eDays = EnumField(choices=['ST', 'MW', 'S', 'M', 'T', 'W', 'R', 'F', 'A'], db_column='eDays', blank=True, null=True)

    dYear = YearField(db_column='dYear')

    nSectionNumber = models.IntegerField(db_column='nSectionNumber', blank=True, null=True)

    cFaculty_ID = models.ForeignKey(FacultyT, models.DO_NOTHING, db_column='cFaculty_ID', blank=True, null=True)
    cRoom_ID = models.ForeignKey(ClassroomT, models.DO_NOTHING, db_column='cRoom_ID', blank=True, null=True)
    nSectionCapacity = models.IntegerField(db_column='nSectionCapacity', blank=True, null=True)
    nEnrolled = models.IntegerField(db_column='nEnrolled', blank=True, null=True)
    bIsBlocked = models.BooleanField(db_column='bIsBlocked', blank=True, null=True)

    tStartTime = TimeField(max_length=4,db_column='tStartTime', blank=True, null=True)
    tEndTime = TimeField(max_length=4, db_column='tEndTime', blank=True, null=True)

    class Meta:
        db_table = 'Section_T'
        unique_together = ('cCoffCode_ID', 'eSession', 'dYear', 'nSectionNumber')

