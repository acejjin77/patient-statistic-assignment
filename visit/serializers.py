from patients.models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('person_id', 'gender_source_value', 'race_source_value', 'ethnicity_source_value', 'year_of_birth')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitOccurrence
        fields = ('person_id', 'visit_occurrence_id', 'visit_concept')


class BirthSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = VisitOccurrence
        fields = ('person_id', 'person')

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        person_representation = representation.pop('person')
        for key in person_representation:
            if (key == 'year_of_birth'):
                representation[key] = person_representation[key]
            else:
                continue
        return representation

    def to_internal_value(self, data):
        person_internal = {}
        for key in PersonSerializer.Meta.fields:
            if key == 'year_of_data':
                person_internal[key] = data.pop(key)

        internal = super().to_internal_value(data)
        internal['person'] = person_internal
        return internal

    def update(self, instance, validated_data):
        person_data = validated_data.pop('person')
        super().update(instance, validated_data)

        person = instance.person
        for attr, value in person_data.items():
            setattr(person, attr, value)
        person.save()

        return instance
