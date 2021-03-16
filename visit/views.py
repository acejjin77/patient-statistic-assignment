from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, serializers
from django.views import generic
from .models import *
from .serializers import *


class VisitChartView(generic.TemplateView):
    template_name = 'visit/visit_concept.html'
    models = VisitOccurrence


class VisitGenderView(generic.TemplateView):
    template_name = 'visit/visit_gender.html'
    models = VisitOccurrence


class VisitRaceView(generic.TemplateView):
    template_name = 'visit/visit_race.html'
    models = VisitOccurrence


class VisitEthnicityView(generic.TemplateView):
    template_name = 'visit/visit_ethnicity.html'
    models = VisitOccurrence


#########################
#                       #
# Visit Occurence Views #
#                       #
#########################


class VisitConceptList(views.APIView):
    def get(self, request, concept_id):
        queryset = VisitOccurrence.objects.filter(visit_concept=concept_id)
        serializer = VisitSerializer(queryset, many=True)
        return Response(serializer.data)


class VisitGenderList(views.APIView):
    def get(self, request, gender):
        queryset = VisitOccurrence.objects.filter(person__gender_concept_id=gender)
        serializer = VisitSerializer(queryset, many=True)
        return Response(serializer.data)


class VisitRaceList(views.APIView):
    def get(self, request, race):
        queryset = VisitOccurrence.objects.filter(person__race_concept_id=race)
        serializer = VisitSerializer(queryset, many=True)
        return Response(serializer.data)


class VisitEthnicityList(views.APIView):
    def get(self, request, ethnicity):
        queryset = VisitOccurrence.objects.filter(person__ethnicity_source_value=ethnicity)
        serializer = VisitSerializer(queryset, many=True)
        return Response(serializer.data)
