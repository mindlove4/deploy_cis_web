from ast import Try
import email
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re
from django.http import HttpResponse
import regex
from django.views.generic import DateDetailView
import os
from .filters import OrderFilter
from cisweb.models import *

# Create your views here.

def home(request):
    return render(request,'home.html')


def cishome1(request):
    return render(request,'teacher_profile2.html') 
    #หน้าป่าวยังไม่เชื่อม 


def responsibiility(request):
    return render(request,'responsibiility.html')



# Create your views here.
def login_student(request):
    return render(request,'login_student.html')
def login_staff(request):
    return render(request,'login_staff.html')
def login_teacher(request):
    return render(request,'login_teacher.html')

def login(request):
    username=request.POST['username']
    password=request.POST['password']
     #login
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/profile')
    else:
        messages.info(request,"Data not found please Try again")
        return HttpResponse(password)

def logout(request):
    auth.logout(request)
    return redirect('/')

def checkdome(request):
    current_user=request.user
    user_email=current_user.email
    regex=r'^[A-Za-z0-9._%+-]+@dome.tu.ac.th$'
    regex_2=r'^[A-Za-z0-9._%+-]+@staff.tu.ac.th$'
    if(re.fullmatch(regex,user_email)):
        return redirect('/profile')
    elif(re.fullmatch(regex_2,user_email)):
        return redirect('/profile')
    else:
        return HttpResponse('No valid')

def profile(request):
    current_user=request.user
    user_email=current_user.email
    try:
        current_teacher=Teacher.objects.get(teacher_id=current_user.username)
    except:
        pass
    try:
        current_teacher=Teacher.objects.get(teacher_email=user_email)
    except:
        pass
    try:
        current_teacher
    except:
        auth.logout(request)
        return HttpResponse('teacher data not found')
    status={0:"Unapprove",1:"Approve"}
    status_value=status[current_teacher.status]

    return render(request,'teacher_profile.html',{'teacher':current_teacher,'status':status_value})
    
def edit_profile(request,pk):
    teacher = Teacher.objects.get(id_card=pk)
    if request.method == "POST":
        try :
            len(request.FILES['img']) != 0
            if len(teacher.teacher_img) > 0:
                try:     
                    os.remove(teacher.teacher_img.path)
                except:
                    pass
            teacher.teacher_img = request.FILES['img']

        except:
            pass

        try: 
            len(request.FILES['certificate']) != 0
            if len(teacher.certificate) > 0:
                try:     
                    os.remove(teacher.certificate.path)
                except:
                    pass
            teacher.certificate = request.FILES['certificate']

        except:
            pass
        
        teacher.teacher_prefix = request.POST.get('prefix')
        teacher.teacher_firstname = request.POST.get('first_name')
        teacher.teacher_lastname = request.POST.get('last_name')
        teacher.teacher_tel = request.POST.get('teacher_tel')
        teacher.teacher_email = request.POST.get('teacher_email')
        teacher.save()
        messages.success(request, "Updated Successfully")
        return redirect('/profile')

    context = {'teacher':teacher}
    return render(request,'edit_profile.html', context)

def train(request):
    train=Coop_Train.objects.all()
    myFilter =  OrderFilter(request.GET,queryset = train)
    context={'filter':myFilter}
    return render(request,'Co-op_train.html',context)   

def traindetails(request,pk):
    train = Coop_Train.objects.get(coop_train_id=pk)
    train_contact=train.train_contact_id
    agenda= Agenda.objects.get(coop_train_id=train)
    context = {'train':train,'contact':train_contact,'agenda':agenda}
    return render(request,'train_details.html',context)

def responsibiility(request):
    current_user=request.user
    user_email=current_user.email
    try:
        teacher=Teacher.objects.get(teacher_id=current_user.username)
    except:
        pass
    try:
        teacher=Teacher.objects.get(teacher_email=user_email)
    except:
        pass
    student_filter=Student.objects.filter(teacher_id=teacher)
    number=len(student_filter)
    context = {'student_filter':student_filter,'number':number}
    return render(request,'responsibiility.html',context)

def student_profile(request,pk):
    student = Student.objects.get(student_id=pk)
    address= Student.address_stu_id
    context = {'student':student,'address':address}
    return render(request,'student_profile.html',context)