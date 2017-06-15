from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


class EmailBackend(object):

    def authenticate(self, username=None, password=None):


        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserMode.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and  user.check_password(password):
                # send_mail(
                #             'User Login',
                #             'Here is the message.',
                #             username,
                #             [username],
                #             fail_silently=False,
                #         )
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
