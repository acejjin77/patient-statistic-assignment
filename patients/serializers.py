from patients.models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('gender_source_value', 'race_source_value', 'ethnicity_source_value')
