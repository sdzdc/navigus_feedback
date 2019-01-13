from django.shortcuts import render,redirect
from .models import *


# Create your views here.


def vForm(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		phone_no = request.POST.get('phone_no')
		email_id = request.POST.get('email_id')
		location = request.POST.get('location')
		feedback = request.POST.get('feedback')
		print(username,phone_no,email_id,location,feedback)
		UserModel.objects.create(username= username,phone_no=phone_no,email_id=email_id,location=location,feedback=feedback)
		return render(request,'end.html',{'context_data':request.POST or None})
	else:
		statelist = State.objects.all()
		states = []
		for state in statelist :
			states.append(state.name)
		return render(request,'form.html',{'statelist':states});