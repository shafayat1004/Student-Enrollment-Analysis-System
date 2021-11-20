from django.db import models

# Create your models here.
class FixedCharField( models.Field ):
    def __init__( self, max_length, *args, **kwargs ):
        self.max_length = max_length
        super().__init__( *args, **kwargs )

    def db_type( self, connection ):
        return 'CHAR( %s )' % self.max_length

class YearField( models.Field ):
    def db_type( self, connection ):
        return 'YEAR'

class TimeField( models.Field ):
    def db_type( self, connection ):
        return 'TIME'

class School ( models.Model ):
    cSchool_ID = models.FixedCharField( max_length = 5 , primary_key = True )
    cSchoolName = models.CharField( max_length = 50 )
