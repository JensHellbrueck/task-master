from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name="projects", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Milestone(models.Model):
    project = models.ForeignKey(
        Project, related_name="milestones", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.name}"


class Task(models.Model):
    milestone = models.ForeignKey(
        Milestone, related_name="tasks", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return f"Task {self.milestone.project.name} - {self.title}"
