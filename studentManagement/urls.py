from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='student-list'),
    path('cadastro', views.StudentCreate.as_view(), name='cadastro')
]
