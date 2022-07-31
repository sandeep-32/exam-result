from django.urls import path
from .views import HomePageView,StudentListView,StudentDetailResult

urlpatterns=[
   path('',HomePageView.as_view(),name='home'),
   path('studentlist/',StudentListView.as_view(),name='studentlist'),
   path('student_detail_result/<int:pk>/',StudentDetailResult.as_view(),name='result_detail'),
]
