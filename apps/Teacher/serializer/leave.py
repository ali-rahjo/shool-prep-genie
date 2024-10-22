from rest_framework import serializers
from apps.Parent.models.leave import Leave

class LeaveStatusUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leave
        fields = ['status']  

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance 