from django.urls import path
from generator import views

urlpatterns=[
path('',views.home,name='home'),
path('generated_password/',views.password,name='password'),
path('about_page/',views.about,name='about'),
]
