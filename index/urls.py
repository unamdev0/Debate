from django.urls import path,include
from index import views

app_name='debate'

urlpatterns=[
    path('login/',views.user_login,name='login'), 
]