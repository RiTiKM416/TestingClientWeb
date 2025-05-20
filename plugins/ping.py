from telethon import events
from telethon.tl.types import Message  # Add this import
import asyncio  # Add this import

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.ping"))
    async def ping_handler(event: Message):  # Now using properly imported Message type
        start = asyncio.get_event_loop().time()
        await event.edit("**Pong!**")
        latency = (asyncio.get_event_loop().time() - start) * 1000
        await event.edit(f"🏓 **Pong!**\n`Latency: {round(latency)}ms`")