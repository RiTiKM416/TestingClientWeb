import os

import json
import asyncio
from pathlib import Path
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import Message

# Import the restart plugin
from plugins.restart_plugin import register_restart_handler

class Userbot:
    def __init__(self):
        # Get all config from environment variables (Railway-friendly)
        self.config = {
            'api_id': int(os.getenv('API_ID')),
            'api_hash': os.getenv('API_HASH'),
            'session_string': os.getenv('SESSION_STRING')  # Added for StringSession
        }
        
        # Initialize client with StringSession
        self.client = TelegramClient(
            session=StringSession(self.config['session_string']),
            api_id=self.config['api_id'],
            api_hash=self.config['api_hash']
        )
        
        # Register the restart handler plugin
        register_restart_handler(self.client)

        self.plugins = []
        self.plugins_dir = Path(__file__).parent / "plugins"

    @staticmethod
    def _load_config(path: str) -> dict:
        with open(path) as f:
            return json.load(f)

    async def _load_plugins(self):
        plugin_files = [f.stem for f in self.plugins_dir.glob("*.py") if f.name != "__init__.py"]
        
        for plugin_name in plugin_files:
            try:
                module = __import__(
                    f"plugins.{plugin_name}", 
                    fromlist=[plugin_name]
                )
                # Initialize plugin if it has an 'initialize' coroutine
                if hasattr(module, 'initialize') and asyncio.iscoroutinefunction(module.initialize):
                    await module.initialize(self)

                self.plugins.append(plugin_name)
                print(f"Loaded plugin: {plugin_name}")
            except Exception as e:
                print(f"Failed to load {plugin_name}: {str(e)}")

    async def start(self):
        await self.client.start()
        print("Userbot started!")
        await self._load_plugins()
        await self.client.run_until_disconnected()

if __name__ == "__main__":
    while True:
        bot = Userbot()
        try:
            restart_needed = asyncio.run(bot.start())
            if not restart_needed:
                break
            print("\n"*3 + "Restarting userbot..." + "\n"*3)
        except Exception as e:
            print(f"Fatal error: {e}")
            break
