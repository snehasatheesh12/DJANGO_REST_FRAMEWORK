"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from myapp.views import *
urlpatterns = [
    #function based view
    path('request_here/',request_here),
    path('get_student/<int:id>/', get_student),  
    #class based view
    path('get_student_here/<int:id>/',StudentApiView.as_view()) ,
    #generic view
    path('student_api_create',StudentCreate.as_view()),
    path('student_api_get/<int:pk>/',StudentRetrive.as_view()),
    path('student_api_update/<int:pk>/',StudentUpdate.as_view()),
    path('student_api_delete/<int:pk>/',StudentDelete.as_view()),
    path('student_api_listcreate',StudentListCreate.as_view()),
    path('student_api_update_retrieve_distroy/<int:pk>',StudentRetrieveUpdateDistroy.as_view()),
    #concrete view
    path('student_List_Api_View',StudentListApiView.as_view()),
    path('student_create_Api_View',StudentCreateApiView.as_view()),
    path('student_retrieve_Api_View/<int:pk>/',StudentRetrieveApiView.as_view()),
    path('student_update_Api_View/<int:pk>/',StudentUpdateApiView.as_view()),
    path('student_distroy_Api_View/<int:pk>/',StudentDistroyApiView.as_view()),
    
    path('student_List_create_Api_View',StudentListCreateApiView.as_view()),
    path('student_retrieve_update_Api_View/<int:pk>/',StudentRetrieveUpdateApiView.as_view()),
    path('student_retrieve_distroy_Api_View/<int:pk>/',StudentRetrieveDistroyApiView.as_view()),
    path('student_retrieve_update_distroy_Api_View/<int:pk>/',StudentRetrieveUpdateDistroyApiView.as_view()),




    





  
]

    
