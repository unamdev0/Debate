from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
	user = models.OneToOneField(User,on_delete='model.cascade')

	def __str__(self):
		return self.user.username
