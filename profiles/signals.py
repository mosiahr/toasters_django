#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Profile

from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print("this is create user profile")

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()