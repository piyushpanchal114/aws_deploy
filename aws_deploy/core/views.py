from django.http.response import HttpResponse
from .models import Employee


def hello(request):
    return HttpResponse("hello")


def get_employee(request):
    queryset = Employee.objects.all()
    return HttpResponse(queryset)
