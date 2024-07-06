from django.urls import path, include
from .views import FacultyViewSet, ProfessorViewSet, StudentViewSet, CourseViewSet


urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='cours_list'),
    path('<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),
    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='student_detail'),
    path('dep/', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('dep/<int:pk>/', FacultyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('professor/<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),
]


