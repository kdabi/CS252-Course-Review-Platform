from django.contrib import admin

# Register your models here.
from .models import Course, Review, Faculty
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('course', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course 
        import_id_fields = ('course_id', 'course_name', 'course_credit', 'course_preReq', 'course_details')
        fields = ('course_id', 'course_name', 'course_credit', 'course_preReq', 'course_details')

class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty 
        import_id_fields = ('fac_name', 'fac_data', 'fac_webpage', 'fac_id')
        fields = ('fac_name', 'fac_data', 'fac_webpage', 'fac_id')

class FacultyAdmin(ImportExportModelAdmin):
    resource_class = FacultyResource


#admin.site.register(Course)
admin.site.register(Course, CourseAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Faculty, FacultyAdmin)
