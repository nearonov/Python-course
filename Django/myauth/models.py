from django.contrib.auth.models import User
from django.db import models


# from django.contrib.auth.models import AbstractUser

# class AdvUser(AbstractUser):
#     image = models.ImageField(upload_to='users_images', blank=True, null=True)

# is_active = models.BooleanField(default=True, verbose_name='Пойшов активаію', db_index=True)
# groups = models.ManyToManyField('auth.Group', verbose_name='groups', blank=True, related_name="adv_user_set")
# user_permissions = models.ManyToManyField(
#     'auth.Permission',
#     verbose_name='specific permissions',
#     blank=True,
#     help_text='Specific permissions for this user.',
#     related_name="adv_user_set_perms",
#     related_query_name="adv_user_perm",
# )

# class Meta(AbstractUser.Meta):
#     pass

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(blank=True, max_length=500)
    agreement_accepted = models.BooleanField(default=False)
