import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession


async def main():
    print("=== Telethon StringSession Generator ===")
    api_id = int(input("Enter your API ID: ").strip())
    api_hash = input("Enter your API HASH: ").strip()

    # This will interactively ask for:
    # 1) Your phone number
    # 2) The login code
    # 3) (Optionally) your 2FA password, if enabled
    client = TelegramClient(StringSession(), api_id, api_hash)
    await client.start()

    session_string = client.session.save()
    print("\n=== Your SESSION_STRING (keep it secret!) ===\n")
    print(session_string)
    print("\nSet this as SESSION_STRING in your Railway environment variables.")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())



