from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User
from django.contrib.auth.password_validation import validate_password
from transaction.models import Cart


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    cart_id = serializers.PrimaryKeyRelatedField(read_only=True, source='cart')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number',
                  'dob', 'password', 'password_confirm', 'is_staff', 'cart_id')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            'dob': {'required': True}
        }
        read_only_fields = ['is_staff', 'cart_id']

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
    cart_id = serializers.PrimaryKeyRelatedField(read_only=True, source='cart')

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'phone_number', 'dob', 'is_staff', 'cart_id']
        read_only_fields = ['id', 'cart_id', 'is_staff', 'email']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False},
            'dob': {'required': False},
        }


class AdminUserUpdate(serializers.ModelSerializer):
    cart_id = serializers.PrimaryKeyRelatedField(read_only=True, source='cart')

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'phone_number', 'dob', 'is_staff', 'cart_id']
        read_only_fields = ('email', 'first_name', 'last_name',
                            'phone_number', 'dob', 'cart_id')


class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(
        write_only=True, required=True)
    cart_id = serializers.PrimaryKeyRelatedField(read_only=True, source='cart')

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'dob',
                  'cart_id', 'current_password', 'new_password', 'new_password_confirm']
        read_only_fields = ('email', 'first_name', 'last_name',
                            'phone_number', 'dob', 'cart_id')

    def validate(self, attrs):
        current_password = attrs.get('current_password')
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')

        if not all([current_password, new_password, new_password_confirm]):
            raise ValidationError(
                {'message': 'current_password, new_password, and new_password_confirm are all required fields and should be present in the input.'})

        if new_password != new_password_confirm:
            raise ValidationError(
                {'message': 'new_password and new_password_confirm fields must match.'})

        if any([key not in ['current_password', 'new_password', 'new_password_confirm'] for key in attrs.keys()]):
            raise ValidationError(
                {'message': 'Only current_password, new_password, and new_password_confirm fields are allowed.'})

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
