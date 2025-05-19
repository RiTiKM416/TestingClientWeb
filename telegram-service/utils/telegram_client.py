from telethon.sync import TelegramClient
from telethon import events
import asyncio
import re

class TelegramService:
    def __init__(self, api_id, api_hash, session_str):
        self.client = TelegramClient(
            StringSession(session_str),
            api_id,
            api_hash,
            connection_retries=3
        )
        self._configure_handlers()

    def _configure_handlers(self):
        @self.client.on(events.NewMessage)
        async def message_handler(event):
            # Add random delay (500-2000ms)
            await asyncio.sleep(random.uniform(0.5, 2.0))
            
            if "notification" in event.text.lower():
                await self._process_notification(event)

    async def _process_notification(self, event):
        """Appears as generic message processing"""
        try:
            # Mimic human response pattern
            async with self.client.action(event.chat_id, 'typing'):
                await asyncio.sleep(1.2)
                await event.reply("Notification received")
        except Exception as e:
            pass

    def run(self):
        with self.client:
            self.client.run_until_disconnected()
