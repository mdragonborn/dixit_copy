import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dixit.settings")
channel_layer = channels.asgi.get_channel_layer()
