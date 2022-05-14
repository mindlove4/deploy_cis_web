from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    class Meta :
        model = Student
        fields = ['student_id','student_prefix','student_firstname','student_lastname','teacher','date_of_birth','campus','education_level','study_year','faculty','major','gpax','student_tel','student_email']
    def get_teacher(self, obj):
        teacher = {
            'teacher_id': obj.teacher_id.teacher_id,
            'teacher_firstname': obj.teacher_id.teacher_firstname,
            'teacher_lastname': obj.teacher_id.teacher_lastname
        }
        return teacher
class Coop_TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coop_Train
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    coop_train = serializers.SerializerMethodField()
    class Meta:
        model = Agenda
        fields = ['agenda_id','coop_train','curriculum','agenda_link']
    def get_coop_train(self, obj):
        coop_train = {
            'coop_train_id': obj.coop_train_id.coop_train_id,
            'intstitute_name': obj.coop_train_id.intstitute_name,
        }
        return coop_train


        