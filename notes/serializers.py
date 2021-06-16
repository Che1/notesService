from django.contrib.auth import get_user_model
from rest_framework import serializers
from notes.models import Note

user_model = get_user_model()

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'subject',
            'text',
            'owner',
        )
