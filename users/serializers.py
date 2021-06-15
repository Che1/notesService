from django.contrib.auth import get_user_model
from rest_framework import serializers

user_model = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ('id', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return user_model.objects.create_user(validated_data['username'], password=validated_data['password'])
