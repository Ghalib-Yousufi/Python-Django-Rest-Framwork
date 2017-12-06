from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Ticket(models.Model):
	SEVERITY_CHOICES = (
		(1, 'Major'),
		(2, 'Critical'),
		(3, 'Minor')
	)
	created = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=100, blank=True, default='')
	severity = models.CharField(max_length=20,choices=SEVERITY_CHOICES, default='')
	assignee = models.ForeignKey('auth.User', related_name='assignee', blank=True)
	reporter = models.ForeignKey('auth.User', related_name='reporter', blank=True)
	is_done = models.BooleanField(default=False)
	done_date = models.DateTimeField(null=True)

	class Meta:
		ordering = ('created',)