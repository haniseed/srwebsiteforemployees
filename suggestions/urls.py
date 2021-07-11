from django.urls import path

from . import views

app_name = "methods"

urlpatterns = [
    path('', views.suggestion_list, name="list"),
    path('recommend', views.give_recommendation, name="recommend"),
    path('<slug>', views.suggestion_detail, name="detail"),
    path('rate/', views.rate_image, name="rate")
]
