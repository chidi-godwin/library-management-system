from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'dob', 'password', 'password_confirm')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'dob': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs
      
    def create(self, validated_data):
        password = validated_data.pop('password')
        password_confirm = validated_data.pop('password_confirm')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'dob']
        
        
class AdminUserUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff']

class UserPasswordUpdate(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['current_password', 'new_password', 'new_password_confirm']
    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
            
    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                "The current password you entered is incorrect.")
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
