from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile, JobPosting
from .serializers import UserProfileSerializer, JobPostingSerializer

class UserProfileView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import logging

logger = logging.getLogger(__name__)

class JobPostingView(APIView):
    def post(self, request):
        
        serializer = JobPostingSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            print("Posting")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Add this line to debug validation issues.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobRecommendationView(APIView):
    def post(self, request):
        
        user_data = request.data
        user_skills = set(user_data.get('skills', []))
        experience_level = user_data.get('experience_level')
        desired_roles = user_data.get('preferences', {}).get('desired_roles', [])
        locations = user_data.get('preferences', {}).get('locations', [])
        job_type = user_data.get('preferences', {}).get('job_type')

        # Filter job postings based on experience level, job type, roles, and location
        job_postings = JobPosting.objects.filter(
            experience_level=experience_level,
            job_type=job_type,
            role__in=desired_roles,
            location__in=locations
        )
        print(job_postings)
        # Further filter jobs by checking if user has at least one required skill
        recommended_jobs = []
        for job in job_postings:
            job_skills = set(job.skills_required)
            if user_skills & job_skills:
                recommended_jobs.append(JobPostingSerializer(job).data)

        return Response(recommended_jobs, status=status.HTTP_200_OK)
