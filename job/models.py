from django.db import models

JOB_TYPE =(
		('Full Time','Full Time'),
		('Part Time','Part Time'),
	)

class Job(models.Model):
	title = models.CharField(max_length=100)
	job_type = models.CharField(max_length=20, choices=JOB_TYPE)
	description = models.TextField()
	published_at = models.DateTimeField(auto_now=True)
	vacancy = models.IntegerField(default=1)
	salary = models.IntegerField(default=0)
	experience = models.IntegerField(default=1)

	def __srt__(self):
		return self.title