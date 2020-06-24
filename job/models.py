from django.db import models
from slugify import slugify
from django.contrib.auth.models import User

JOB_TYPE =(
		('Full Time','Full Time'),
		('Part Time','Part Time'),
	)

def image_upload(instance,filename):
	imagename , extension = filename.split(".")
	return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):
	owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	job_type = models.CharField(max_length=20, choices=JOB_TYPE)
	description = models.TextField()
	published_at = models.DateTimeField(auto_now=True)
	vacancy = models.IntegerField(default=1)
	salary = models.IntegerField(default=0)
	experience = models.IntegerField(default=1)
	category = models.ForeignKey('Category',on_delete=models.CASCADE)
	image = models.ImageField(upload_to = image_upload)
	slug = models.SlugField(blank=True,null=True)

	def __str__(self):
		return self.title

	def save(self,*args,**kwargs):
		self.slug = slugify(self.title)
		super(Job,self).save(*args,**kwargs)

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Apply(models.Model):
	job = models.ForeignKey(Job,related_name='apply',on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	website = models.URLField()
	cv = models.FileField(upload_to='aplly/')
	cover_leter = models.TextField()
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
