from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistation
from .models import User
from django.urls import reverse
# Create your views here.
def add_show(request):
	
	
	if request.method == 'POST':
		form = StudentRegistation(request.POST)
		if form.is_valid():
			nm = form.cleaned_data['name']
			em = form.cleaned_data['email']
			pw = form.cleaned_data['password']
			reg = User(name=nm,email=em,password=pw)
			reg.save()
			form = StudentRegistation()
	else:
		form = StudentRegistation()
	student = User.objects.all()
		
	return render(request,'crud_app/addandshow.html',{'form':form,'student':student})
def delete_student(request,id):
	if request.method == 'POST':
		delete = User.objects.get(pk=id)
		delete.delete()
		return HttpResponseRedirect('/')
def update_data(request,id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		form = StudentRegistation(request.POST,instance=pi)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('add_show'))
	else:
		pi = User.objects.get(pk=id)
		form = StudentRegistation(instance=pi)
	return render(request,'crud_app/updatestudent.html',context={'form':form})