from telethon import events
import os
import aiohttp
import sys
import asyncio

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.restart", outgoing=True))
    async def restart_handler(event):
        """Railway-optimized restart command"""
        try:
            msg = await event.reply("🔄 Initiating restart...")
            
            # 1. Trigger Railway redeploy
            api_token = os.getenv('RAILWAY_API_TOKEN')
            if not api_token:
                return await msg.edit("❌ RAILWAY_API_TOKEN not set")

            headers = {"Authorization": f"Bearer {api_token}"}
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.railway.app/v1/deployments",
                    headers=headers
                ) as response:
                    if response.status == 201:
                        await msg.edit("✅ Success! New deployment starting...")
                    else:
                        error = await response.text()
                        await msg.edit(f"❌ Failed: {error}")
            
            # 2. Graceful shutdown
            await bot.client.disconnect()
            
        except Exception as e:
            await event.reply(f"💥 Critical error: {str(e)}")
