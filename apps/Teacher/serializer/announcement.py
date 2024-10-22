from rest_framework import serializers
from apps.Teacher.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'date', 'announcement']

    def create(self, validated_data):
        # Access the user from the context
        request = self.context.get('request')
        validated_data['created_by'] = request.user  # Set the created_by field
        announcement = Announcement.objects.create(**validated_data)
        return announcement

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # No conversion needed since date is already a DateField
        representation['date'] = instance.date  # Just return the date
        return representation
