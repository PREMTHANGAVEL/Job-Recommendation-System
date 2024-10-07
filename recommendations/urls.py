from django.urls import path
from .views import UserProfileView, JobPostingView, JobRecommendationView

urlpatterns = [
    path('user-profiles/', UserProfileView.as_view(), name='user_profiles'),
    path('job-postings/', JobPostingView.as_view(), name='job_postings'),
    path('recommend-jobs/', JobRecommendationView.as_view(), name='recommend_jobs'),
]
