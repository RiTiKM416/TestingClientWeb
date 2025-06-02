import asyncio
import time
from telethon import events
from telethon.tl import types

async def initialize(bot):
    @bot.client.on(events.NewMessage(pattern=r"\.info", outgoing=True))
    async def info_handler(event):
        start_time = time.time()
        msg = await event.edit("🔍 **Starting system scan...**")
        await asyncio.sleep(2)
        
        # Stage 1: Fetching basic stats
        await msg.edit("📡 **Connecting to Telegram servers...**")
        await asyncio.sleep(2)
        
        # Stage 2: Collecting data
        await msg.edit("📂 **Compiling account statistics...**")
        await asyncio.sleep(2)
        
        # Get dialogs and process data
        dialogs = await bot.client.get_dialogs()
        groups = channels = group_admin = channel_admin = group_owner = channel_owner = 0
        me = await bot.client.get_me()
        
        for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, types.Chat):
                groups += 1
                # Check admin status in groups
                try:
                    participant = await bot.client.get_permissions(entity, me)
                    if participant.is_admin:
                        group_admin += 1
                    if participant.is_creator:
                        group_owner += 1
                except:
                    pass
                    
            elif isinstance(entity, types.Channel):
                if entity.broadcast:
                    channels += 1
                    # Check admin status in channels
                    try:
                        participant = await bot.client.get_permissions(entity, me)
                        if participant.is_admin:
                            channel_admin += 1
                        if participant.is_creator:
                            channel_owner += 1
                    except:
                        pass
                else:
                    groups += 1
                    # Check admin status in supergroups
                    try:
                        participant = await bot.client.get_permissions(entity, me)
                        if participant.is_admin:
                            group_admin += 1
                        if participant.is_creator:
                            group_owner += 1
                    except:
                        pass
        
        # Calculate processing time
        process_time = round(time.time() - start_time, 2)
        
        # Final formatted output
        result = (
            f"📊 **Account Analysis Complete** 📊\n\n"
            f"👥 **Group Statistics**\n"
            f"├ Total Groups: `{groups}`\n"
            f"├ Admin Positions: `{group_admin}`\n"
            f"└ Owner Positions: `{group_owner}`\n\n"
            f"📢 **Channel Statistics**\n"
            f"├ Total Channels: `{channels}`\n"
            f"├ Admin Positions: `{channel_admin}`\n"
            f"└ Owner Positions: `{channel_owner}`\n\n"
            f"⏱️ Processed in `{process_time}s`\n"
            f"✅ Account ID: `{me.id}`"
        )
        
        await msg.edit(result)
