from django.shortcuts import render,redirect
from . models import Signup,Gallery
from . forms import SignupForm,LoginForm,UpdatForm
from django.contrib import messages
from django.contrib.auth import logout as logouts
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method =='POST':
        f=SignupForm(request.POST or None,request.FILES or None)
        if f.is_valid():
            name=f.cleaned_data['Name']
            age=f.cleaned_data['Age']
            place=f.cleaned_data['Place']
            photo=f.cleaned_data['Photo']
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"email allready exist")
                return redirect('/register')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Email=email,Password=password,Photo=photo) 
                tab.save()
                messages.success(request,'registration success')
                return redirect('/')
    else:
        f=SignupForm()
    return render(request,'register.html',{'form':f})  


def login(request):
    if request.method =='POST':
        f=LoginForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data['Email']
            password=f.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"user dosnot exists")
                return redirect('/login')
            elif user.Password != password:
                messages.warning(request,'password incorrect')
                return redirect('/login')
            else:
                return redirect('/home/%s'% user.id)      
    else:
        f=LoginForm()
    return render(request,'login.html',{'form':f})

def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def update(request,id):
	user=Signup.objects.get(id=id)
	if request.method=='POST':
		f=UpdatForm(request.POST or None,request.FILES or None,instance=user)
		if f.is_valid():
			name=f.cleaned_data['Name']
			age=f.cleaned_data['Age']
			place=f.cleaned_data['Place']
			photo=f.cleaned_data['Photo']
			email=f.cleaned_data['Email']
			f.save()
			return redirect('/home/%s' % user.id)
	else:
		f=UpdatForm(instance=user)
	return render(request,'update.html',{'f':f,'user':user})	


def logout(request):
	logouts(request)
	messages.success(request,'logedout successfully')
	return redirect('/')


def gallery(request):
    details=Gallery.objects.all()
    return render(request,'gallery.html',{'data':details})
def imgdetails(request,id):
    data=Gallery.objects.get(id=id)
    return render(request,'imgdetails.html',{'data':data})












