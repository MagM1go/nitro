import aiohttp
import asyncio
import string
import random


a = int(input('How many codes you delivering?: '))

invalid_links = []
valid_links = []

async def main():
    for i in range(a):
        j = "".join([i for i in string.ascii_letters + string.digits])
        codes = "".join(random.choices(j, k=16))
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{codes}?with_application=false&with_subscription_plan=true') as response:
                try:
                    print(f"Invalid (https://discord.gift/{codes})")
                    invalid_links.append(codes)
                except:
                    print(f"Valid: https://discord.gift/{codes}")
                    valid_links.append(f'https://discord.gift/{codes}')
    print(f"""

Valid links: {len(valid_links)}
Invalid links: {len(invalid_links)}

All valid links: {"".join(valid_links) or "Nothing find."}

""")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

input('Press any key for exit')
