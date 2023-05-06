from django.urls import path
from . import views

urlpatterns = [ 
path('', views.login_view, name='login_view'),
path('register/', views.register, name='register'),
path('student/', views.student, name='student'),
path('teacher/', views.teacher, name='teacher'),
path('headdep/', views.headdep, name='headdep'),
path('users/', views.UserAPIView.as_view(), name="users"),
path('users/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user'),
]