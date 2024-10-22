# In apps/parent/views/email.py

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

def verify_email(request, uidb64, token):
    
    print('verification------------')
    try:
       
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        
       
        if default_token_generator.check_token(user, token):
            user.is_active = True 
            user.save()
            return HttpResponse("Email verified successfully.")
        else:
            return HttpResponse("Token is invalid or expired.")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    return HttpResponse("Invalid verification link.")
