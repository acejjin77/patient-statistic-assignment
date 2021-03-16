from patients import models
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('person_id', 'gender_source_value', 'race_source_value', 'ethnicity_source_value', 'year_of_birth')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VisitOccurrence
        fields = ('person_id', 'visit_occurrence_id', 'visit_concept')
