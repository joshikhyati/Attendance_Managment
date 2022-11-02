import uuid
from datetime import date, datetime

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Employee,Attendance,Timespend

from django.contrib.auth.decorators import login_required,user_passes_test

def index(request):
    return render(request,'index.html')

#uses_passes_test give condition if user login only following function show
@user_passes_test(lambda u: u.is_superuser,login_url='/login_user/')
def create_employee(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        fathername=request.POST['fathername']
        mothername=request.POST['mothername']
        phonenumber=request.POST['phonenumber']
        emergencynumber=request.POST['emergencynumber']
        bloodgroup=request.POST['bloodgroup']
        address=request.POST['address']
        position=request.POST['position']
        user_id=request.POST['user_id']
        email=request.POST['email']
        password=request.POST['password1']
        confirmpassword=request.POST['password2']
        code=str(uuid.uuid4().int)[:4]
        if password==confirmpassword:
            try:
                    user=User.objects.create_user(username=user_id, email=email, password=password)
                    user.save()
                    
                    employee=Employee.objects.create(fullname=fullname, fathername=fathername, mothername=mothername, 
                    phonenumber=phonenumber,emergencynumber=emergencynumber, bloodgroup=bloodgroup, address=address, 
                    position=position, user_id=user, code=code)
                    employee.save() 
                    
                    messages.success(request, "This Employee register successfuly" )
                    return redirect('/create_employee/')
            except Exception as e:
                print (str(e))
                messages.success(request, "This Employee already register" )
                return render(request, 'register.html' )
    return render(request,'register.html' )


def login_user(request):
    if request.method=="POST":
        user_id=request.POST['user_id']
        password=request.POST['password1']
        user_obj=authenticate(request,username=user_id,password=password)
        if user_obj is  None:
            messages.success(request,"wrong username or password")
            redirect('/login_user/')
        else:
            login(request,user_obj)
            f_name=user_obj.first_name
            return redirect('/dashboard/')
# is_authenticated use to keep user logged in
    if request.user.is_authenticated:
        return redirect('/dashboard/',)
    return render(request,'login.html')


@login_required(login_url='/login_user/')
def signout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/login_user/')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='/login_user/')
def timespend(request):
    if request.method=="POST":
        emp1 = Employee.objects.get(user_id=request.user)
        #start_timer fetch punchin time return data thru json response
        if request.POST.get('start_timer'):
            date=datetime.today()
            punchin=datetime.now()
            try:
                if emp1:
                        attendance, created  = Attendance.objects.get_or_create(employee=emp1,date=date)
                        if created:
                            attendance.save()
                        ts=Timespend.objects.create(attendance=attendance,punchin=punchin)
                        ts.save()
                response = {'success': True}
            except Exception as e:
                print (str(e))
                messages.success(request,"user is not valid")
                response = {'success': False}
    #stop_timer fetchout timer return data thru json response
        if request.POST.get('stop_timer'):
            attendance=Attendance.objects.filter(employee=emp1).last()
            stop_timer_time = datetime.now()
            ts = Timespend.objects.latest()
            ts.punchout = stop_timer_time
            ts.save()
            response = {'sucsess': True}
        return JsonResponse(response)
    return render(request, 'timespend.html')