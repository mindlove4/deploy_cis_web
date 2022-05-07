from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator,MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Address_Student(models.Model):
    address_stu_id= models.AutoField(primary_key=True)
    house_number= models.CharField(max_length=255)
    village_name= models.CharField(max_length=255,null=True, blank=True)
    soi = models.CharField(max_length=255,null=True, blank=True)
    road = models.CharField(max_length=255)
    subdistrict= models.CharField(max_length=255) 
    district= models.CharField(max_length=255)
    province= models.CharField(max_length=255)
    postcode= models.IntegerField(validators=[MaxValueValidator(99999),MinValueValidator(9999)])

class Teacher(models.Model):
    teacher_id= models.CharField(primary_key=True,max_length=255)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_prefix= models.CharField(max_length=10)
    teacher_firstname= models.CharField(max_length=255)
    teacher_lastname= models.CharField(max_length=255)
    id_card= models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    role= models.CharField(max_length=255)
    status= models.BooleanField()
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    teacher_tel = models.CharField(validators=[phone_regex,MinLengthValidator(9)], max_length=10)
    teacher_email= models.EmailField(max_length=255)
    teacher_img= models.ImageField(upload_to=filepath, null=True, blank=True)
    certificate= models.ImageField(upload_to=filepath, null=True, blank=True)


class Student(models.Model):
    student_id= models.CharField(primary_key=True,max_length=255)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id= models.ForeignKey(Teacher, on_delete=models.CASCADE)
    address_stu_id= models.ForeignKey(Address_Student, on_delete=models.CASCADE)
    student_prefix= models.CharField(max_length=10)
    student_firstname= models.CharField(max_length=255)
    student_lastname= models.CharField(max_length=255)
    student_img= models.ImageField(upload_to=filepath, null=True, blank=True)
    date_of_birth= models.DateField()
    id_card= models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    campus= models.CharField(max_length=255)
    education_level= models.CharField(max_length=255)
    study_year= models.CharField(max_length=2)
    faculty= models.CharField(max_length=255)
    major= models.CharField(max_length=255)
    gpax= models.DecimalField(max_digits=3,decimal_places=2,null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    student_tel = models.CharField(validators=[phone_regex,MinLengthValidator(9)], max_length=10)
    student_email= models.EmailField(max_length=255)


class Train_Contact(models.Model):
    train_contact_id=models.AutoField(primary_key=True)
    institute_number=models.CharField(max_length=255)
    institute_name=models.CharField(max_length=255)
    soi=models.CharField(max_length=255,null=True, blank=True)
    road=models.CharField(max_length=255,null=True, blank=True)
    subdistrict=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    province=models.CharField(max_length=255)
    postcode= models.IntegerField(validators=[MaxValueValidator(99999)])
    phone_regex = RegexValidator(regex=r'^\d{9,15}$')
    institute_tel = models.CharField(validators=[phone_regex,MinLengthValidator(9)], max_length=10,null=True, blank=True)
    institute_email=models.EmailField(max_length=255,null=True, blank=True)

class Coop_Train(models.Model):
    coop_train_id=models.AutoField(primary_key=True)
    train_contact_id=models.ForeignKey(Train_Contact, on_delete=models.CASCADE)
    intstitute_name=models.CharField(max_length=255)
    curriculum=models.CharField(max_length=255,null=True, blank=True)
    datetime_event=models.CharField(max_length=255,null=True, blank=True) 
    start_apply=models.DateField(null=True, blank=True)
    deadline_apply=models.DateField(null=True, blank=True)
    amount= models.CharField(max_length=255,null=True, blank=True) 
    location=models.CharField(max_length=255) 
    cost=models.IntegerField(validators=[MaxValueValidator(99999)])
    link_detail=models.CharField(max_length=255,null=True, blank=True)

class Agenda(models.Model):
    agenda_id=models.AutoField(primary_key=True)
    coop_train_id=models.ForeignKey(Coop_Train, on_delete=models.CASCADE)
    curriculum=models.CharField(max_length=255)
    agenda_link=models.CharField(max_length=255)



