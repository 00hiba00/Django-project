from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
# Create your views here.

def index(request):
    return render(request,'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()               # all users from the DB
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()         
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer