from django.utils import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

#Comparing token for email verification
class TokenGenerator(PasswordResetTokenGenerator): #Inheriting from PasswordResetTokenGenerator
    def _make_hash_value(self,user,timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))


account_activation_token=TokenGenerator()
