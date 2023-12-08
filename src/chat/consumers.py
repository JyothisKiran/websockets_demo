import json
from django.contrib.auth.models import AnonymousUser
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        user = await self.get_user()
        if user != AnonymousUser():
            print('authorised') 
        # Leave room group
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        user = await self.get_user()
        print(user)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # user = login(self.scope, u)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @database_sync_to_async
    def get_user(self):
        return self.scope["user"]
    
    @database_sync_to_async
    def get_user_for_token(self,token):
        try:
            user = User.objects.get(auth_token=token)
            return user
        except User.DoesNotExist:
            return False
        




 # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # self.room_group_name = "chat_%s" % self.room_name
        # print(self.scope['headers'])
        # listss = []
        # for i in self.scope["headers"]:
        #     listss.append({key.decode('utf-8'): value.decode('utf-8') for key, value in [i]})

        # # print("lists = ",listss)
        # # checking_header_token = any("token" in d for d in listss)
        # # print("checking_header_token = ",checking_header_token)
        # for d in listss:
        #     if 'token' in d:
        #         token = (d['token'])
        #         user = await self.get_user_for_token(token)
        #         if not user:
        #             await self.close()
        #         await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        #         await self.accept()
        #     else:
        #         self.close()
