import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

import one.routing
import two.routing
import threechat.routing

#from one.routing import ws_urlpatterns
#from two.routing import ws_urlpatterns
#from threechat.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examplechannels.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(
            URLRouter([
                one.routing.ws_urlpatterns,
                two.routing.ws_urlpatterns,
                threechat.routing.ws_urlpatterns
            ]))),
    }
)


