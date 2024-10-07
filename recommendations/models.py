from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    skills = models.JSONField()  # Store skills as a list of strings
    experience_level = models.CharField(max_length=100)
    desired_roles = models.JSONField()  # Store roles as a list of strings
    locations = models.JSONField()  # Store locations as a list of strings
    job_type = models.CharField(max_length=50)

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    skills_required = models.JSONField()  # Store required skills as a list of strings
    experience_level = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
