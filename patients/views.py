from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, serializers
from django.views import generic
from . import models, serializers


class PatientChartView(generic.TemplateView):
    template_name = 'patients/patients_all.html'
    models = models.Person


#########################
#                       #
# Person Views          #
#                       #
#########################

class PersonList(views.APIView):
    def get(self, request):
        queryset = models.Person.objects.all()
        serializer = serializers.PersonSerializer(queryset, many=True)
        return Response(serializer.data)


class PersonGenderList(views.APIView):
    def get(self, request, gender):
        queryset = models.Person.objects.filter(gender_source_value=gender)
        serializer = serializers.PersonSerializer(queryset, many=True)
        return Response(serializer.data)


class PersonRaceList(views.APIView):
    def get(self, request, race):
        queryset = models.Person.objects.filter(race_source_value=race)
        serializer = serializers.PersonSerializer(queryset, many=True)
        return Response(serializer.data)


class PersonEthnicityList(views.APIView):
    def get(self, request, ethnicity):
        queryset = models.Person.objects.filter(ethnicity_source_value=ethnicity)
        serializer = serializers.PersonSerializer(queryset, many=True)
        return Response(serializer.data)
