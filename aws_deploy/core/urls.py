from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("employee/", views.get_employee, name="get-employee"),
]
