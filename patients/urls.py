from django.urls import path, re_path
from patients import views

app_name = 'patients'
urlpatterns = [
    path('patients/', views.PatientChartView.as_view(), name='patients'),
    path('visit/', views.VisitChartView.as_view(), name='visit'),
]
