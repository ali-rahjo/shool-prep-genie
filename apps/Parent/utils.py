from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes


def send_verification_email(user, request):
   
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_url = f"{request.scheme}://{request.get_host()}/api/v1/parent/verify-email/{uid}/{token}/"

   
    user.email_user(
        subject="Welcome To SchoolPrep Genie",
        message=f"Click the link to verify your email: {verification_url}"
    )
