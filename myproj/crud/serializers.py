from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'name', 'email', 'password', 'user_created']
        fields = '__all__'
        # extra_kwargs = {
        #     'password': {'write_only': True},  # Prevents password from being shown in responses
        #     'user_created': {'read_only': True}  # Auto-generated, cannot be modified
        # }    