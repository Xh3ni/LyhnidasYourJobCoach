from django.contrib import admin
from .models import Job, Applicants, Selected
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):

    list_display = ('recruiter', 'title', 'slug', 'company')
    search_fields = ['company', 'title']
    list_filter = ('company', 'country', 'title')


@admin.register(Applicants)
class ApplicantsAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'date_posted')
    search_fields = ['applicant', 'job']
    list_filter = ('applicant', 'job')


admin.site.register(Selected)
