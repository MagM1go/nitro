import aiohttp # pip install aiohttp
import asyncio # pip install asyncio
import string # Встроенная библиотека
import random # Встроенная библиотека


a = int(input('How many codes you delivering?: ')) # Думаю не стоит говорить, что это

invalid_links = [] 
valid_links = [] # Этих двух массивой то же самое касается

endl = '\n'

async def main(): # Создание асинхронной функции
    for i in range(a): # Цикл
        j = "".join([i for i in string.ascii_letters + string.digits]) # Проходимся по буковкам и циферкам
        codes = "".join(random.choices(j, k=16)) # Рандомим их
        async with aiohttp.ClientSession() as session: # Создание сессии
            async with session.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{codes}?with_application=false&with_subscription_plan=true') as response: # Получение запроса уже
                try:
                    print(f"Invalid (https://discord.gift/{codes})") 
                    invalid_links.append(codes)
                except:
                    print(f"Valid: https://discord.gift/{codes}")
                    valid_links.append(f'https://discord.gift/{codes}') # 6 Строк выше обычная проверка и занесение в массив
    print(f'Valid links: {len(valid_links)}\nInvalid links: {len(invalid_links)}\nAll valid links: {endl.join(valid_links) or "Nothing find."}') # <- Результат всего этого

loop = asyncio.get_event_loop()
loop.run_until_complete(main()) # Эти три строки для запуска 
loop.close()

input('Press any key for exit') # На случай, если вы будете компилировать в .exe как я

# P.S. Это нерабочее, поскольку тут обычный рандом, настоящие генераторы караются баном аккаунта дискорд! Данный "Генератор" обычный розыгрыш, можете давать друзьям чисто по фану, если они у вас, конечно, не прошаренные в этой теме.
