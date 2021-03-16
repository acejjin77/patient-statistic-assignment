from django.urls import path, re_path
from visit import views

app_name = 'visit'
urlpatterns = [
    path(r'', views.VisitChartView.as_view(), name='visit'),
    path(r'visit_concept_id/<str:concept_id>', views.VisitConceptList.as_view(), name='visit-data-concept'),
]
