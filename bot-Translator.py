# Any editing of this file and
# pretending to be the creator of the file is illegal .
#
#rubika: @silentAw
#Telegram: @silentAw
#
# این سورس کد حاصل زحمت یه برنامه نویس هست
# اگه قراره اسم چنل رو عوض کنی و خودتو سازنده
# سازنده سورس جلوه بدی مادرت اسفند رو 29 روز
# جندگی میکنه چون 29 روزه دیگه خود دانی.

from rubpy import Client, handlers, Message, models
from requests import get
import asyncio


B_green = "\033[1;32m"
B_yellow = "\033[1;33m"
message1= "New message: - text"
message2 = "New message: - robot"
loading = "❲  Database loading ❳ • ⌬"
robot = "سلام، لطفا برای ترجمه متن انگلیسی ، اول متن خود ( - ) بگذارید و بعد متن مورد نظرتون رو وارد کنید.\n مثال:\n - hello [⫹⫺](https://rubika.ir/@im_Next)"
async def main():
    
    async with Client(session="Login-4") as client:
        
        @client.on(handlers.MessageUpdates())
        
        async def updates(message: Message):
        
            text = message.raw_text
            
            if text != None and text.startswith('-'):
                			
                			text = message.raw_text.replace("-","")
                			
                			await message.reply(loading)
                			
                			
                			gpt = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={text}").json()['result']
                			
                			
                			await message.reply(gpt)
                			
                			print(B_green,message1)
                			
            elif text != None and text =="ربات":
                
                await message.reply(robot)
                
                print(B_yellow,message2)
                
        await client.run_until_disconnected()
        
asyncio.run(main())# Made by silentAw
