# Generated by Django 3.0.3 on 2021-03-16 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('concept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('concept_name', models.CharField(max_length=255)),
                ('domain_id', models.CharField(max_length=20)),
                ('vocabulary_id', models.CharField(max_length=20)),
                ('concept_class_id', models.CharField(max_length=20)),
                ('standard_concept', models.CharField(blank=True, max_length=1, null=True)),
                ('concept_code', models.CharField(max_length=50)),
                ('valid_start_date', models.DateField()),
                ('valid_end_date', models.DateField()),
                ('invalid_reason', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'concept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionOccurrence',
            fields=[
                ('condition_occurrence_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('condition_start_date', models.DateField(blank=True, null=True)),
                ('condition_start_datetime', models.DateTimeField()),
                ('condition_end_date', models.DateField(blank=True, null=True)),
                ('condition_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('stop_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_occurrence_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('condition_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_status_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'condition_occurrence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrugExposure',
            fields=[
                ('drug_exposure_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('drug_exposure_start_date', models.DateField(blank=True, null=True)),
                ('drug_exposure_start_datetime', models.DateTimeField()),
                ('drug_exposure_end_date', models.DateField(blank=True, null=True)),
                ('drug_exposure_end_datetime', models.DateTimeField()),
                ('verbatim_end_date', models.DateField(blank=True, null=True)),
                ('stop_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('refills', models.IntegerField(blank=True, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('days_supply', models.IntegerField(blank=True, null=True)),
                ('sig', models.TextField(blank=True, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=50, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('drug_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('route_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('dose_unit_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'drug_exposure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('year_of_birth', models.IntegerField()),
                ('month_of_birth', models.IntegerField(blank=True, null=True)),
                ('day_of_birth', models.IntegerField(blank=True, null=True)),
                ('birth_datetime', models.DateTimeField(blank=True, null=True)),
                ('location_id', models.BigIntegerField(blank=True, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('care_site_id', models.BigIntegerField(blank=True, null=True)),
                ('person_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('race_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('ethnicity_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VisitOccurrence',
            fields=[
                ('visit_occurrence_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('visit_start_date', models.DateField(blank=True, null=True)),
                ('visit_start_datetime', models.DateTimeField()),
                ('visit_end_date', models.DateField(blank=True, null=True)),
                ('visit_end_datetime', models.DateTimeField()),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('care_site_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('admitted_from_concept_id', models.IntegerField()),
                ('admitted_from_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('discharge_to_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'visit_occurrence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='+', serialize=False, to='patients.Person')),
                ('death_date', models.DateField()),
                ('death_datetime', models.DateTimeField(blank=True, null=True)),
                ('death_type_concept_id', models.IntegerField()),
                ('cause_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'death',
                'managed': False,
            },
        ),
    ]
