from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User') #este es un vinculo con otro modelo.
	title = models.CharField(max_length=200) # defines un texto con un número limitado de caracteres.
	text = models.TextField() #esto es para textos largos sin un limite
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
