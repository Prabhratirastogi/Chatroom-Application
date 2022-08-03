import os
import django
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddleware, AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})

# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","djangochat.settings")
# django.setup()
# application = get_default_application()