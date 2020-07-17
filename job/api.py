from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import generics

@api_view(['GET'])
def joblistapi(request):
	job_list = Job.objects.all()
	data = JobSerializer(job_list, many = True).data
	return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,id):
	job_detail = Job.objects.get(id=id)
	data = JobSerializer(job_detail).data
	return Response({'data':data})



class JobDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = JobSerializer
	queryset = Job.objects.all()
	lookup_field = 'id'