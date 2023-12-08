import os
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from token_auth_app.consumers import TokenAuthConsumer 
from chat.middlewares import QueryAuthMiddleware


from chat.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {

        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            QueryAuthMiddleware(
                URLRouter
                ([
                    path("", TokenAuthConsumer.as_asgi()),
                ] + websocket_urlpatterns)
            )
        ),
    }

)
