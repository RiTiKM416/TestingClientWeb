from telethon import events
from telethon.tl.types import Message
import time
from datetime import datetime
import asyncio
import re

# Configuration (Edit these values)
GROUP_ID = -1002531112998  # Your target group ID
LOG_GROUP_ID = -1002629087320  # Your log group ID
RESPONSE_TEXT = """Device name : Iphone 14 plus
udid : 00008110-00187460363A401E"""
COOLDOWN_SECONDS = 600  # 10 minutes cooldown
ARTIFICIAL_DELAY = 2  # 2 seconds

# Precompile regex pattern for efficiency
TRIGGER_REGEX = re.compile(
    r'(\b|.*?)giveaway.*?first.*?1.*?udid.*?win.*?certificate',
    re.IGNORECASE | re.DOTALL
)

# State tracking
last_trigger_time = 0

async def initialize(bot):
    @bot.client.on(events.NewMessage(
        chats=[GROUP_ID], 
        incoming=True
    ))
    async def giveaway_hunter(event: Message):
        global last_trigger_time
        
        if event.out:
            return
            
        # Check message against regex pattern
        if not TRIGGER_REGEX.search(event.raw_text):
            return
            
        current_time = time.time()
        
        if current_time - last_trigger_time < COOLDOWN_SECONDS:
            return
            
        try:
            # Add human-like delay
            await asyncio.sleep(ARTIFICIAL_DELAY)
            
            # Send response
            response = await event.reply(
                RESPONSE_TEXT,
                reply_to=event.id,
                link_preview=False
            )
            
            last_trigger_time = current_time
            
            # Enhanced logging
            trigger_time = datetime.fromtimestamp(event.date.timestamp()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            response_delay = (response.date.timestamp() - event.date.timestamp()) * 1000
            
            log_message = (
                f"🎉 Giveaway Triggered!\n"
                f"🕒 Trigger Time: {trigger_time}\n"
                f"⏱️ Response Delay: {response_delay:.2f}ms\n"
                f"👤 User: {event.sender_id}\n"
                f"📌 Group: {GROUP_ID}\n"
                f"🔗 Message Link: https://t.me/c/{str(abs(GROUP_ID))[4:]}/{event.id}\n"
                
            )
            
            if LOG_GROUP_ID != -1:
                await bot.client.send_message(
                    LOG_GROUP_ID,
                    log_message,
                    link_preview=False
                )
                
        except Exception as e:
            error_log = f"❌ Error at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:\n{str(e)}"
            print(error_log)
            if LOG_GROUP_ID != -1:
                await bot.client.send_message(LOG_GROUP_ID, error_log)
