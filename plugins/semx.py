from telethon import events
import asyncio

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.sex", outgoing=True))
    async def sex_handler(event):
        try:
            msg = await event.edit("🔄 **Processing command...**")
            
            stages = [
                "👔 Removing princesse's clothes...",
                "🍆 princess taking my peenar...",
                 "loded princess pussy with my white sauce.\n"
                 "Princess is pregnent 🤰. ")
            ]

            for stage in stages:
                await asyncio.sleep(5)
                await msg.edit(stage)
                
        except Exception as e:
            await event.edit(f"⚠️ System Malfunction: {str(e)}")  
