from rest_framework import serializers
from apps.Parent.models.parent import Parent
from apps.User.serializer.user import UserSerializer

class ParentProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()  
    profile_image = serializers.ImageField(required=False)
    profile_image_url = serializers.SerializerMethodField()


    class Meta:
        model = Parent
        fields = ['id', 'user', 'address', 'phone_number', 'gender',  'profile_image','profile_image_url']  
        
    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)  
        return None    