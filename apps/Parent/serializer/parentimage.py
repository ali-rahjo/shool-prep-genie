from rest_framework import serializers
from apps.Parent.models.parent import Parent


class ParentImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parent
        fields = ['profile_image']
        
    def update(self, instance, validated_data):
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance