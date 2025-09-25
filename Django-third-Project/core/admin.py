from django.contrib import admin
from .models import Developer, Project, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [SkillInline]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('developers',)  # برای انتخاب راحت‌تر در ادمین

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
