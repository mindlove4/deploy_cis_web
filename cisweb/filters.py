from dataclasses import fields
from pyexpat import model
import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Coop_Train
        fields = '__all__'