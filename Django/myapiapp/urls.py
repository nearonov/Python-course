from django.urls import path, include
from myapiapp.views import CourseListView, CourseDetailView, CourseViewSet, api_courses
from rest_framework.routers import DefaultRouter

app_name = 'myapiapp'

router = DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('products/', CourseListView.as_view(), name='course_list'),
    # path('products/', api_courses, name='course_list'),
    path('products/<pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('', include(router.urls))

]
