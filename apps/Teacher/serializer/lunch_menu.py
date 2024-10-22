from rest_framework import serializers
from apps.Teacher.models.lunch_menu import LunchMenu



class LunchMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchMenu
        fields = ['id','week_start_date','week_end_date', 'lunch_menu' ]
