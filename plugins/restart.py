from telethon import events
import sys
import os
import asyncio
import subprocess

async def restart_handler(event):
    """Restart via Railway API without Project ID"""
    try:
        # Get Railway API Token (MUST be set in env vars)
        api_token = os.getenv('RAILWAY_API_TOKEN')
        if not api_token:
            await event.reply("❌ RAILWAY_API_TOKEN not configured")
            return

        # New API endpoint that doesn't require Project ID
        deploy_url = "https://api.railway.app/v1/deployments"
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(deploy_url, headers=headers) as resp:
                if resp.status == 201:
                    await event.reply("✅ Restart triggered! New deployment starting...")
                else:
                    error = await resp.text()
                    await event.reply(f"❌ Failed (HTTP {resp.status}): {error}")

        await bot.client.disconnect()

    except Exception as e:
        await event.reply(f"💥 Critical error: {str(e)}")
