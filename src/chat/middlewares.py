from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from .consumers import ChatConsumer
from django.http import parse_cookie

User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class QueryAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, app):
        # Store the ASGI application we were passed
        self.app = app

    async def __call__(self, scope, receive, send):
        # Look up user from query string (you should also do things like
        # checking if it is a valid user ID, or if scope["user"] is already
        # populated).
        print(scope)
        check_flag = 0
        for name, value in scope.get("headers", []):
            print(name, value)
            if name == b"token":
                check_flag = 1
                print(value.decode('utf-8'))
                scope['user'] = await ChatConsumer.get_user_for_token(value.decode('utf-8'))
        if check_flag == 0 :
            raise ValueError('No token found in Headers')

        return await self.app(scope, receive, send)

