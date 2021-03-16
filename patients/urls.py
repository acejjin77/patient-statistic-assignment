from django.urls import path, re_path
from patients import views

app_name = 'patients'
urlpatterns = [
    path(r'', views.PatientChartView.as_view(), name='patients'),
    path(r'whole_patient/', views.PersonList.as_view(), name='person-data'),
    path(r'gender/<str:gender>', views.PersonGenderList.as_view(), name='person-data-gender'),
    path(r'race/<str:race>', views.PersonRaceList.as_view(), name='person-data-race'),
    path(r'ethnicity/<str:ethnicity>', views.PersonEthnicityList.as_view(), name='person-data-ethnicity'),
]
