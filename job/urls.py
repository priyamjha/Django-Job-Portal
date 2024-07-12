from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('applied-jobs/', views.applied_jobs, name='applied-jobs'),
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    path('update-job/<int:pk>/', views.update_job, name='update-job')
]
