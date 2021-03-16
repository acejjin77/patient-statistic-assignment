from patients.models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('gender_source_value', 'race_source_value', 'ethnicity_source_value')


class DeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Death
        fields = ('person_id', 'death_date')
