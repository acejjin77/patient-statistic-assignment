from django.urls import path, re_path
from patients import views

app_name = 'patients'
urlpatterns = [
    path(r'patients/', views.PatientChartView.as_view(), name='patients'),
    path(r'visit/', views.VisitChartView.as_view(), name='visit'),
    path(r'personlist/', views.PersonList.as_view(), name='person-data'),
]
