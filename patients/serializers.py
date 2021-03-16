from patients import models
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('person_id', 'gender_source_value', 'race_source_value', 'ethnicity_source_value')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VisitOccurrence
        fields = ('person_id', 'visit_occurrence_id', 'visit_type_concept_id')
