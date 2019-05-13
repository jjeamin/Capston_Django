from django.urls import path
from . import views

urlpatterns = [
	path('coding/', views.st_coding, name='st_coding'),
	path('subject/',views.st_subject, name='st_subject'),
]
