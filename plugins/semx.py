from telethon import events
import asyncio

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.sex", outgoing=True))
    async def sex_handler(event):
        try:
            msg = await event.edit("🔄 **Processing command...**")
            
            stages = [
                "🌌 Teleporting you to special room...",
                "🚪 Russian agent inbound...",
                "👙 She's getting naked...",
                "👔 Removing your clothes...",
                "🍆 She saw your peenar...",
                "😱 Visibly terrified...",
                "📏 Trying to measure...",
                ("❌ **Execution Failed**\n"
                 "🚨 Error 404: Size mismatch detected Too Big to insert\n"
                 "🇷🇺 Russian girl gone home.\n"
                 "💡 Recommendation: cut your peenar 😕")
            ]

            for stage in stages:
                await asyncio.sleep(5)
                await msg.edit(stage)
                
        except Exception as e:
            await event.edit(f"⚠️ System Malfunction: {str(e)}")
