# from django.db import models

# # Create your models here.

# from django.contrib.auth.models import User, AnonymousUser
# from django.db.models import SET
# from config.settings import AUTH_USER_MODEL


# class Message(models.Model):
#     """"
#     model for storing mesages (chat)
#     """
#     sender_user = models.ForeignKey(AUTH_USER_MODEL, related_name='sender', on_delete=SET(AnonymousUser.id))
#     receiver_user =  models.ForeignKey(AUTH_USER_MODEL, related_name='receiver', on_delete=SET(AnonymousUser.id))
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)


# class Room(models.Model):
#     """
#     model for chat room
#     """
#     sender_user = models.ForeignKey(AUTH_USER_MODEL, related_name='room_sender', on_delete=SET(AnonymousUser.id))
#     receiver_user =  models.ForeignKey(AUTH_USER_MODEL, related_name='room_receiver', on_delete=SET(AnonymousUser.id))
#     room_name = models.CharField(max_length=200, unique=True)

#     def __str__(self) -> str:
#         return self.room_name
