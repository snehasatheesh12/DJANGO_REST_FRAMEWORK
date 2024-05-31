from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .serailizers import StudentSerializer
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator




#concrete view class
class StudentListApiView(ListAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
class StudentCreateApiView(CreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveApiView(RetrieveAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentUpdateApiView(UpdateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')    
class StudentDistroyApiView(DestroyAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer


class StudentListCreateApiView(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

@method_decorator(csrf_exempt, name='dispatch')    
class StudentRetrieveUpdateApiView(RetrieveUpdateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    
@method_decorator(csrf_exempt, name='dispatch')    
class StudentRetrieveDistroyApiView(RetrieveDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    
@method_decorator(csrf_exempt, name='dispatch')    
class StudentRetrieveUpdateDistroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    



#generic apiview
class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetrieveUpdateDistroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
      return self.retrieve(request,*args,**kwargs)
     
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class StudentList(GenericAPIView,ListModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)



class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)



class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

#class based api view
class StudentApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data is created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id=None,*args,**kwargs):
        if id is None:
            return Response({'msg':'Id is required'},status=status.HTTP_400_BAD_REQUEST)
        stu=student.objects.get(id=id)
        seriailzer=StudentSerializer(stu,data=request.data)
        if seriailzer.is_valid():
            seriailzer.save()
            return Response({'msg':'data is updated'},status=status.HTTP_201_CREATED)
        return Response({'msg':'not updated'},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None, *args, **kwargs):
        try:
            if id is not None:
                stu = student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data, status=status.HTTP_302_FOUND)
        except ObjectDoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request, id=None, *args, **kwargs):
      try:
          if id is not None:
            stu=student.objects.get(id=id)
            stu.delete()
            return Response({'msg':'data is deleted'},status=status.HTTP_204_NO_CONTENT)
      except ObjectDoesNotExist:
            return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

#function based api view
@api_view(['POST','GET'])
def request_here(request):
   if request.method == 'POST':
       m=request.data.get("name",None)
       if m is None:
           return Response({'msg':"data field is required"},status=status.HTTP_400_BAD_REQUEST)
       return Response({'msg':m})
   if request.method == 'GET':
       print(request.data)
       return Response({'msg':"get data"})
   
@api_view(['POST','GET','PUT','DELETE','PATCH'])
def get_student(request,id):
   if request.method == 'POST':
        serailizer=StudentSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':'data is craeted'})
        return Response(serailizer.errors)
   if request.method == 'PUT':
        stu=student.objects.get(pk=id)
        serailizer=StudentSerializer(stu,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':"data updated"})
        return Response(serailizer.errors)
   if request.method == 'PATCH':
        stu=student.objects.get(id=id)
        serailizer=StudentSerializer(stu,data=request.data,partial=True)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':"data updated partially"})
        return Response(serailizer.errors)
   if request.method == 'DELETE':
        stu = student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data is deleted'})
   try:
        stu = student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)
   except student.DoesNotExist:
        return Response({'msg': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

