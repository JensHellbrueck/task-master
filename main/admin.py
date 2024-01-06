from django.contrib import admin

from .models import Project, Milestone, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("owner",)


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "created_at")
    search_fields = ("name", "project__name")
    list_filter = ("project",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def project_name(self, obj):
        return obj.milestone.project.name

    list_display = (
        "title",
        "milestone",
        "project_name",
        "completed",
        "priority",
    )
    search_fields = ("title", "milestone__name")


admin.site.site_header = "R4S TaskMaster Admin"
admin.site.site_title = "R4S TaskMaster Admin Portal"
