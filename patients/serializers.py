from patients import models
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('person_id', 'gender_source_value', 'person_source_value', 'ethnicity_source_value')


class DeathSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Death
        fields = ('person_id',)
