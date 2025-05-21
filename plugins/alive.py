import time
import asyncio
from telethon import events
from datetime import datetime

# Plugin metadata
VERSION = "1.0.1"
start_time = time.time()

async def initialize(bot):
    # Store deployment time
    deployment_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @bot.client.on(events.NewMessage(pattern=r"\.alive", outgoing=True))
    async def alive_handler(event):
        try:
            # Initial response
            msg = await event.edit("🔍 Running system diagnostics...")
            
            # First ping test
            start1 = time.time()
            await bot.client.get_me()
            ping1 = round((time.time() - start1) * 1000, 1)
            await msg.edit(f"📊 Initializing diagnostics:\n🏓 First Ping: {ping1}ms")
            await asyncio.sleep(2)
            
            # Second ping test
            start2 = time.time()
            await bot.client.get_me()
            ping2 = round((time.time() - start2) * 1000, 1)
            await msg.edit(f"📊 Running diagnostics:\n🏓 First Ping: {ping1}ms\n🏓 Second Ping: {ping2}ms")
            await asyncio.sleep(2)
            
            # Third ping test
            start3 = time.time()
            await bot.client.get_me()
            ping3 = round((time.time() - start3) * 1000, 1)
            
            # Calculate uptime
            uptime_seconds = time.time() - start_time
            hours, rem = divmod(uptime_seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            uptime = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
            
            # Final status message
            final_msg = (
                f"⚡ **Userbot Operational** ⚡\n\n"
                f"📈 **Performance Metrics:**\n"
                f"• Initial Ping: {ping1}ms\n"
                f"• Secondary Ping: {ping2}ms\n"
                f"• Current Ping: {ping3}ms\n\n"
                f"📦 **System Info:**\n"
                f"• Version: {VERSION}\n"
                f"• Last Deployment: {deployment_time}\n"
                f"• Uptime: {uptime}\n\n"
                f"✅ All systems nominal"
            )
            await msg.edit(final_msg)
            
        except Exception as e:
            await event.edit(f"❌ Diagnostic failure: {str(e)}")
            raise
