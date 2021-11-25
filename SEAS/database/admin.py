from django.contrib import admin

# Register your models here.
from database import models

class ClassroomAdmin(admin.ModelAdmin):  
    model = models.ClassroomT
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.ClassroomT,  ClassroomAdmin)


class FacultyAdmin(admin.ModelAdmin):
    model = models.FacultyT

    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.FacultyT, FacultyAdmin)


class SchoolAdmin(admin.ModelAdmin):
    model = models.SchoolT
    
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.SchoolT, SchoolAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    model = models.DepartmentT
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.DepartmentT, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    model = models.CourseT
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.CourseT, CourseAdmin)


class CofferedCourseAdmin(admin.ModelAdmin):
    model = models.CoofferedcourseT
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]
    
admin.site.register(models.CoofferedcourseT, CofferedCourseAdmin)


class SectionAdmin(admin.ModelAdmin):
    model = models.SectionT
    list_display = [field.name for field in model._meta.fields]
    search_fields = [model._meta.pk.name]

admin.site.register(models.SectionT, SectionAdmin)

