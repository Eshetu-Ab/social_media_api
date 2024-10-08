# Importing the necessary modules
from rest_framework import serializers  # Import serializers from Django REST framework
from .models import Hashtag  # Import the Hashtag model from the current app's models

# Defining the HashtagSerializer class
class HashtagSerializer(serializers.ModelSerializer):
    # This serializer converts Hashtag model instances to and from JSON format

    class Meta:
        model = Hashtag  # Specify the model to be serialized
        fields = ['id', 'name', 'posts']  # Specify the fields to be included in serialization
        read_only_fields = ['posts']  # Make the 'posts' field read-only, so it's not required during creation
