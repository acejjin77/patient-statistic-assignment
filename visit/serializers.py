from patients.models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('person_id', 'gender_source_value', 'race_source_value', 'ethnicity_source_value')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitOccurrence
        fields = ('person_id', 'visit_occurrence_id', 'visit_concept')
