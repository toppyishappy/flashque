from django.conf import settings


class Line():
    def __init__(self):
        self.channel_secret = settings.CHANNEL_SECRET
        self.channel_access_token = settings.CHANNEL_ACCESS_TOKEN