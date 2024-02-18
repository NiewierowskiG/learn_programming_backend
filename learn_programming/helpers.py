from .models import User
from rest_framework_simplejwt.tokens import AccessToken


def get_user_by_token_request(request):
    token_obj = AccessToken(request.headers['Authorization'][7:])
    user = User.objects.get(pk=token_obj['user_id'])
    return user
