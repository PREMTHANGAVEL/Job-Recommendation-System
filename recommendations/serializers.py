from rest_framework import serializers
from .models import UserProfile, JobPosting

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


from rest_framework import serializers
from .models import JobPosting  # Assuming you have a JobPosting model defined

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['title', 'skills_required', 'role', 'location', 'job_type', 'experience_level']
