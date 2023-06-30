from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	date_done = models.DateTimeField(null=True, blank=True)
	is_important = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} - by {self.user.username}'