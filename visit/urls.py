from django.urls import path, re_path
from visit import views

app_name = 'visit'
urlpatterns = [
    path(r'', views.VisitChartView.as_view(), name='visit'),
    path(r'gender/', views.VisitGenderView.as_view(), name='gender'),
    path(r'race/', views.VisitRaceView.as_view(), name='race'),
    path(r'ethnicity/', views.VisitEthnicityView.as_view(), name='ethnicity'),
    path(r'visit_concept_id/<str:concept_id>', views.VisitConceptList.as_view(), name='visit-data-concept'),
    path(r'visit_gender/<str:gender>', views.VisitGenderList.as_view(), name='visit-data-gender'),
    path(r'visit_race/<str:race>', views.VisitRaceList.as_view(), name='visit-data-race'),
    path(r'visit_ethnicity/<str:ethnicity>', views.VisitEthnicityList.as_view(), name='visit-data-ethnicity'),
]
