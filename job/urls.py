from django.urls import path
from . import views
from . import api



app_name = 'job'
urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add', views.add_job,name='add_job'),
    path('<str:slug>', views.job_detail,name='job_detail'),

    #Api
    path('api/list', api.joblistapi,name='joblistapi'),
    path('api/jobs/<int:id>', api.job_detail_api,name='job_detail_api'),
    path('api/jobs/v2/<int:id>', api.JobDetail.as_view(),name='job_detail_api'),
]
