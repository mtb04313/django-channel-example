#import time
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
#from channels.generic.websocket import WebsocketConsumer
from one.bussiness import Domain

#class OneConsumer(WebsocketConsumer):
class OneConsumer(AsyncWebsocketConsumer):
 
    #def connect(self):
    async def connect(self):
        #self.accept()
        await self.accept()
        D = Domain()
        for i in range(100):
            data = D.do(i)
            
            #self.send(data)
            await self.send(data)
            
            # time.sleep(2)
            await sleep(2)
            
    #def disconnect(self, close_code):
    async def disconnect(self, code):
        pass
        