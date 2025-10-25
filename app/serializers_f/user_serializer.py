from rest_framework import serializers
from app.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone_number']
        read_only_fields = ['email_verified', 'is_admin', 'is_staff', 
                            'is_active','is_owner','created_at','updated_at']

    def email_verification(self, user):
        email = getattr(user, "email", None)
        if not email:
            return False
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "phone_number", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            phone_number=validated_data["phone_number"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
    
class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['id','email','phone_number','email_verified', 'is_admin', 'is_staff', 'is_active','is_owner']
        # write_only_fields = ['password'] 


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)