from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group = 'game_%s' % self.game_id
        async_to_sync(self.channel_layer.group_add)(
            self.game_group,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group,
            self.channel_name
        )
        pass

    def receive(self, text_data):
        message = json.loads(text_data)
        print(message)

        async_to_sync(self.channel_layer.group_send)(
            self.game_group,
            {
                'type' : 'game_update',
                'message' : message
            }
        )

    def game_update(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
