from django.shortcuts import render
from rest_framework import views
from django.views import generic
from patients import models
import numpy as np
import sklearn


class PatientChartView(generic.TemplateView):
    template_name = 'patients/patients_all.html'
    models = models.Person
    seri

class VisitChartView(generic.TemplateView):
    template_name = 'visit/visit_all.html'
    models = models.VisitOccurrence
