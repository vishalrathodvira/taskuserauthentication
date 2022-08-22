from ast import Not
from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import employeeForm

from .models import employee
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if User.objects.filter(username=username):
            messages.error(request,'Username already exist! Please try some other username.')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
            
        if password != cpassword:
            messages.error(request,"Passwords didn't matched!!")
            return redirect('signup')

        if len(username)>20:
            messages.error(request,"Username must be under 20 charcters!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request,"user name must be alpha-numeric!")
            return redirect('signup')

        myuser=User.objects.create_user(username,email,password)
        myuser.fname=fname
        myuser.lname=lname
        myuser.save()
        messages.success(request,"Your Account has been created succesfully!!")
        return render(request,'signin.html')

    return render (request,"signup.html")

def signin(request):

    if request.method == 'POST':
        username=request.POST['username']
        passw=request.POST['pass']
        
        user=authenticate(username=username,password=passw)
        if user is not None :
            login(request,user)
            messages.success(request,'you are successfully login')
            data=User.objects.all()
           
            return render(request,'home.html')
        else:
            messages.error(request,"pleause check your email or password")
            redirect('signin')



    return render (request,'signin.html')
def profile(request):
    if request.method == 'POST':
        img=request.POST['img']
        bio=request.POST['bio']
        fname=request.POST['fname']
        mname=request.POST['mname']
        lname=request.POST['lname']
        number=request.POST['number']
        dob=request.POST['dob']
        email=request.POST['email']
        country=request.POST['country']
        state=request.POST['state']
        dist=request.POST['dist']
        edu=request.POST['edu']
        college=request.POST['college']
        year=request.POST['year']
        mark=request.POST['mark']
        role=request.POST['role']
        duration=request.POST['duration']
        sal=request.POST['sal']
        media=request.POST['media']
        link=request.POST['link']



        v=employee(img=img,bio=bio,fname=fname,mname=mname,lname=lname,number=number,dob=dob,email=email,country=country,state=state,dist=dist,edu=edu,college=college,year=year,mark=mark,role=role,duration=duration,sal=sal)
        v.save()
        emp=employee.objects.all()
        data={
        'emp':emp}
        return render(request,'index.html',{'data':data})
    return render(request,'index.html',{'data':data})
def show(request):
    emp=employee.objects.all()
    data={
        'emp':emp}
    return render(request,'index.html',{'data':data})

def delete(request,id):
    emp=employee.objects.get(id=id)
    emp.delete()
    return redirect('show')


def edit(request,id):
    item = employee.objects.get(pk=id)
    form = employeeForm(request.POST or None, instance=item)
    if form.is_valid():
            form.save()
            return redirect('show') 
    return render(request,'edit.html',{'item':item,'form':form})
   
 
        
