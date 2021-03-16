from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, serializers
from django.views import generic
from . import models, serializers
import numpy as np
import sklearn


class PatientChartView(generic.TemplateView):
    template_name = 'patients/patients_all.html'
    models = models.Person


class VisitChartView(generic.TemplateView):
    template_name = 'visit/visit_all.html'
    models = models.VisitOccurrence


class PersonList(views.APIView):
    def get(self, request):
        queryset = models.Person.objects.all()
        serializer = serializers.PersonSerializer(queryset)
        return Response(serializer.data)

    def get_gender(self, gender):
        return models.Person.objects.filter(gender_source_value=gender)

    def get_race(self, race):
        return models.Person.objects.filter(race_source_value=race)

    def get_ethnicity(self, ethnicity):
        return models.Person.objects.filter(ethnicity_source_value=ethnicity)

