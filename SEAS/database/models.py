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
