from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, serializers
from django.views import generic
from . import models, serializers


class VisitChartView(generic.TemplateView):
    template_name = 'visit/visit_concept.html'
    models = models.VisitOccurrence

#########################
#                       #
# Visit Occurence Views #
#                       #
#########################


class VisitConceptList(views.APIView):
    def get(self, request, concept_id):
        queryset = models.VisitOccurrence.objects.filter(visit_concept=concept_id)
        serializer = serializers.VisitSerializer(queryset, many=True)
        return Response(serializer.data)

