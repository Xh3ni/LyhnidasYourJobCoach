from django.contrib import admin
from .models import Profile, Skill, AppliedJobs, SavedJobs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('user',)}
    list_display = ('full_name', 'slug', 'country', 'looking_for')
    search_fields = ['country', 'looking_for']
    list_filter = ('user', 'looking_for')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill')
    search_fields = ['user', 'skill']
    list_filter = ('user', 'skill')


admin.site.register(AppliedJobs)
admin.site.register(SavedJobs)
