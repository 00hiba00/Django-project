from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['url', 'username', 'email', 'password','groups']
    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])  # Remove groups from validated_data
        password = validated_data.pop('password')       # Remove password from validated_data

        user = User(**validated_data)                   # Create user without password
        user.set_password(password)                     # Hash password
        user.save()

        if groups_data:                                # Set many-to-many groups
            user.groups.set(groups_data)
        
        return user
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'