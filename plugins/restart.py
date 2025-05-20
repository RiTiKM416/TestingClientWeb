from telethon import events
import sys
import os
import asyncio
import subprocess

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.restart", outgoing=True))
    async def restart_handler(event):
        """Restart the userbot with updates"""
        try:
            # 1. Send restart notification
            msg = await event.reply("🔄 Restarting userbot...")
            
            # 2. Update code from Git (optional)
            # Uncomment these lines if using Git:
            # proc = await asyncio.create_subprocess_exec(
            #     'git', 'pull',
            #     stdout=asyncio.subprocess.PIPE,
            #     stderr=asyncio.subprocess.PIPE
            # )
            # await proc.communicate()
            
            # 3. Prepare fresh start
            await bot.client.disconnect()
            
            # 4. Restart using same python executable
            os.execl(sys.executable, sys.executable, "-m", "userbot")
            
        except Exception as e:
            await event.reply(f"❌ Restart failed: {str(e)}")
            raise