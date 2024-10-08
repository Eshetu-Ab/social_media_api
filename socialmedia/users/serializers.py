# users/serializers.py
from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'location', 'website', 'cover_photo']  # Include new fields

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()  # Nested serializer for user profile

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile']  # Include the profile

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        # Update the user instance
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update the UserProfile instance
        profile_instance = instance.userprofile
        profile_instance.bio = profile_data.get('bio', profile_instance.bio)
        profile_instance.avatar = profile_data.get('avatar', profile_instance.avatar)
        profile_instance.location = profile_data.get('location', profile_instance.location)
        profile_instance.website = profile_data.get('website', profile_instance.website)
        profile_instance.cover_photo = profile_data.get('cover_photo', profile_instance.cover_photo)
        profile_instance.save()

        return instance
