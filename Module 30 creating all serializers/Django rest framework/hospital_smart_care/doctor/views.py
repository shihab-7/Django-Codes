from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, AvailableTime,Designation,Specialization,Review
from .serializers import DoctorSerializer, DesignationSerializer,SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer

# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        doctor_id = self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(doctor=doctor_id)
        return queryset


