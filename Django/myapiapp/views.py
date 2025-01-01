from rest_framework import generics
from shop.models import *
from myapiapp.serializers import *
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET'])
def api_courses(request: HttpRequest):
    if request.method == 'GET':
        courses = Course.objects.all()
        serialize = CourseSerializer(courses, many=True)
        return Response(serialize.data)
