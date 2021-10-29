from allauth.account.apps import AccountConfig
from allauth.socialaccount.apps import SocialAccountConfig


class ModifiedAccountConfig(AccountConfig):
    default_auto_field = 'django.db.models.BigAutoField'


class ModifiedSocialAccountConfig(SocialAccountConfig):
    default_auto_field = 'django.db.models.BigAutoField'
