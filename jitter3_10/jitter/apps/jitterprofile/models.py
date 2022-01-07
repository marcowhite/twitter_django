from django.db import models

from django.contrib.auth.models import User

class JitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.jitterprofile = property(lambda u:JitterProfile.objects.get_or_create(user=u)[0])
