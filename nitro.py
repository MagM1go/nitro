import asyncio # built-in
import string # built-in
import random # built-in

import aiohttp # pip install aiohttp


invalid_links = []
valid_links = []
check_url = f'https://discordapp.com/api/v9/entitlements/gift-codes/{codes}?with_application=false&with_subscription_plan=true'
alphabet = "".join([i for i in string.ascii_letters + string.digits])  # Создаём массив с английским алфавитом
endl = '\n'


async def send_get(url: str) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession() as session:
        return await session.get(url)
    

async def main(code_count: int):  # Создание асинхронной функции
    for i in range(code_count):  # Цикл
        gift_code = "".join(random.choices(j, k=16))  # Рандомим их
        gift_url = f"https://discord.gift/{gift_code}"
        response:  = await send_get(check_url)
        parsed_response: dict = await response.json()
        received_code: int = parsed_response.get("code")

        if code == 10038:
            print(f"Invalid ({gift_url})") 
            invalid_links.append(gift_code)
            continue

        print(f"Valid: {gift_url}")
        valid_links.append(gift_url)  # 6 Строк выше обычная проверка и занесение в массив

    print(f'Valid links: {len(valid_links)}\n'
          f'Invalid links: {len(invalid_links)}\n'
          f'All valid links: {endl.join(valid_links) or "Nothing find."}')  # <- Результат всего этого


if __name__ == "__main__":
    codes_count = int(input('How many codes you delivering?: '))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(code_count=codes_count))  # Эти три строки для запуска 
    loop.close()
    
    input('Press any key for exit') # На случай, если вы будете компилировать в .exe как я

# P.S. Это нерабочее, поскольку тут обычный рандом, настоящие генераторы караются баном аккаунта дискорд! 
# (жаль, что их существование по определению невозможно и нужно другие пути для получения халявного нитра)
# Данный "Генератор" обычный розыгрыш, можете давать друзьям чисто по фану, если они у вас, конечно, не прошаренные в этой теме.
