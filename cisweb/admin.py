from django.contrib import admin
from .models import Address_Student,Teacher,Student,Train_Contact,Coop_Train,Agenda

class StudentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Student._meta.fields]
admin.site.register(Student,StudentAdmin)

class Address_StudentAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Address_Student._meta.fields]
admin.site.register(Address_Student,Address_StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Teacher._meta.fields]
admin.site.register(Teacher,TeacherAdmin)


class Coop_TrainAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Coop_Train._meta.fields]
admin.site.register(Coop_Train,Coop_TrainAdmin)

class Train_ContactAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Train_Contact._meta.fields]
admin.site.register(Train_Contact,Train_ContactAdmin)

class AgendaAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Agenda._meta.fields]
admin.site.register(Agenda,AgendaAdmin)
