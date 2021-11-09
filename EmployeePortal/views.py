from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmployeeBasicInfo
from .employee import employee
from .serializers import EmployeeBasicInfoSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/images/',
        '/api/employee/',
        '/api/employee/create/',
        '/api/employee/delete/<id>',
        '/api/employee/<update>/<id>',
        '/api/employee/<id>',
        '/api/employee/new',
    ]

    return Response(routes)

@api_view(['GET'])
def getEmployeeBasicInfo(request):
    employee = EmployeeBasicInfo.objects.all().order_by('-id')
    serializer = EmployeeBasicInfoSerializer(employee, many=True)
    return Response(serializer.data)
