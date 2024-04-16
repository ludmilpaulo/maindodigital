from django.db import models
from django.contrib.auth.models import User
from courses.models import Subject 

class Task(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
	documentation = models.FileField(upload_to='project_documents/%Y/%m/%d', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	datecompleted = models.DateTimeField(null=True, blank=True)
	important = models.BooleanField(default=False)
	development_url = models.URLField(blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title



