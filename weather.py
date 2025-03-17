import aiohttp
from bs4 import BeautifulSoup

async def get_weather():
    # URL Yandex.Погода для Екатеринбурга
    url = "https://yandex.ru/pogoda?lat=56.8380127&lon=60.59747314"

    # Асинхронно отправляем GET-запрос на сайт
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # Асинхронно получаем HTML-код страницы
                html = await response.text()

                # Разбираем страницу с помощью BeautifulSoup
                soup = BeautifulSoup(html, 'html.parser')

                # Находим элемент с текущей температурой
                temperature = soup.find('span', class_='temp__value').text

                # Возвращаем результат
                return f'Текущая температура в Екатеринбурге: {temperature}°C'
            else:
                return f'Не удалось получить данные о погоде для Екатеринбурга'

