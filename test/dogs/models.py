from django.db import models

# Create your models here.
from djongo import models
from django.utils.timezone import now


# Create your models here.

class DogsData(models.Model): #collection name
	SEX_CHOICES = [("M", "Male"), ("F", "Female")]
	spayed_or_neutered_CHOICE = [("yes","YES") , ("no","NO")]

	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	#Documents
	dog_name = models.CharField(max_length=20, null=True)
	gender = models.CharField(choices=SEX_CHOICES, max_length=1, null=True)
	breed = models.CharField(max_length=30, blank=True)
	birth = models.DateTimeField(auto_now_add=False, auto_now=False)
	dominant_color = models.CharField(max_length=20, blank=False)
	secondary_color = models.CharField(max_length=20, blank=True)
	third_color = models.CharField(max_length=20, blank=True)
	spayed_or_neutered = models.CharField(choices=spayed_or_neutered_CHOICE, max_length=1,  default='yes')
	guard_or_trained = models.CharField(choices=spayed_or_neutered_CHOICE, max_length=1, null='no')
	borough = models.CharField(max_length=30, blank=False, null=False)
	zip_code = models.IntegerField(null=False)

	def __str__(self):
		return self.name

		

