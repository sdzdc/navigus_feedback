from django.db import models

# Create your models here.

class State(models.Model):
	name = models.CharField('state',max_length=400)

	class Meta:
		verbose_name = 'Location'

	def __str__(self):
		return self.name 


class UserModel(models.Model):
	username = models.CharField('username',max_length=60)
	phone_no = models.CharField('phone_no',max_length=60)
	email_id = models.CharField('email_id',max_length=128)
	location = models.CharField('location',max_length=60)
	feedback = models.TextField('feedback',max_length=500)

	class Meta:
		verbose_name = 'Feedback'

	def __str__(self):
		return self.username

	def clean_username(self,*args,**kwargs):
		username = self.cleaned_data.get('username')
		if(len(username) > 60):
			raise forms.ValidationError('Username should not be greater than 60 letters')
		if(username == ''):
			raise forms.ValidationError('Username should not be empty')
		return fname

	def clean_feedback(self,*args,**kwargs):
		feedback = self.cleaned_data.get('feedback')
		if(len(feedback) > 10):
			raise forms.ValidationError('Feedback should not be greater than 500 letters')
		if(feedback == ''):
			raise forms.ValidationError('Feedback should not be empty')   
		return feedback

	def clean_email_id(self,*args,**kwargs):
		email_id = self.cleaned_data.get('email_id')
		if(len(email_id) > 128):
			raise forms.ValidationError('Email should not be greater than 128 letters')
		if(email_id == ''):
			raise forms.ValidationError('Email should not be empty')   
		return email_id

	def clean_phone_no(self,*args,**kwargs):
		phone_no = self.cleaned_data.get('phone_no')
		if(len(phone_no) > 60):
			raise forms.ValidationError('Phone Number should not be greater than 60 letters')
		if(phone_no == ''):
			raise forms.ValidationError('Phone Number should not be empty')   
		return phone_no						
	