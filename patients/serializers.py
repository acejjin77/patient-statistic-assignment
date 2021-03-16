from patients import models
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('gender_source_value', 'race_source_value', 'ethnicity_source_value')
