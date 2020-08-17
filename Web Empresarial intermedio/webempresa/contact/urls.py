from django.urls import path
from . import views

urlpatterns = [
    # path de contact
    path('', views.contact, name="contact"),

]
