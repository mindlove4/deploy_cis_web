from rest_framework import viewsets,routers
from .models import *
from .serializer import *

router = routers.DefaultRouter()



class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Coop_TrainApiView(viewsets.ModelViewSet):
    queryset = Coop_Train.objects.all()
    serializer_class = Coop_TrainSerializer

class AgendaApiView(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


router.register(r'student/list' , StudentApiView)
router.register(r'coop_train/list' , Coop_TrainApiView)
router.register(r'agenda/list' , AgendaApiView)
