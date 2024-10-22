from rest_framework import serializers
from apps.Parent.models.writemsg import WriteMsg


class MessageResponseUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WriteMsg
        fields =  ['id','response']
    def update(self, instance, validated_data):
        instance.response = validated_data.get("response", instance.response)
        instance.save()
        return instance
