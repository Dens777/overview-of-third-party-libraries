import requests
import pandas as pd
import numpy as np
from PIL import Image, ImageFilter


class Requests: # Погода в Казани на следующие 5 дней

    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.7887,
        "longitude": 49.1221,
        "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
        "timezone": "Europe/Moscow"
    }

    for i in range(1, 6):
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()

            temp_min = data['daily']['temperature_2m_min'][i]
            temp_max = data['daily']['temperature_2m_max'][i]
            precipitation = data['daily']['precipitation_sum'][i]
            forecast_date = data['daily']['time'][i]

            print(f"Прогноз погоды в Казани на {forecast_date}")
            print(f"Минимальная температура: {temp_min}°C")
            print(f"Максимальная температура: {temp_max}°C")
            print(f"Ожидаемое количество осадков: {precipitation} мм")
            print(' ')

        else:
            print(f"Ошибка {response.status_code}: {response.text}")



access_key = '4e05d137-0a8c-4a25-b16f-5fbc9ed1816b' # Данные Яндекс.Погода

headers = {
    'X-Yandex-Weather-Key': access_key
}

response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=52.37125&lon=4.89388', headers=headers)

print('Данные Яндекс Погода, ключ до 10.10.2024')
print(response.json())

for i in range (100):
    print ('-', end='')
print('\n')

class Pandas:
    # Загрузка данных из текстового файла
    data = pd.read_fwf(r'C:\Users\dens7\PycharmProjects\lesson0\module_11\data_11')
    print(data.head(2)) # Выводит на консоль первыу две строки
    print('')
    print(data.tail(2)) # Выводит на консоль последние две строки'''


for i in range (100):
    print ('-', end='')
print ("\n")

class Numpy:
    arr = np.random.randint(2, 50, size=20)
    sum = np.sum(arr)
    flip = np.flip(arr)
    sort = np.sort(arr)

    print(arr)
    print(sum)
    print(flip)
    print(sort)


for i in range(100):
    print('-', end='')
print('\n')

class Pillow:
    image = Image.open(r'C:\Users\dens7\PycharmProjects\lesson0\module_11\Urban Logo.jpg')
    resized_image = image.resize((800, 600))  # изменение размера на 800 x 600 пикселей
    resized_image.save('resized_image.jpg')

    image = Image.open(r'C:\Users\dens7\PycharmProjects\lesson0\module_11\Urban Logo.jpg')
    blurred_image = image.filter(ImageFilter.CONTOUR)  # применить эффекты
    blurred_image.save('blurred_image.jpg')

#сохранить в другой формат
    image = Image.open(r'C:\Users\dens7\PycharmProjects\lesson0\module_11\Urban Logo.jpg')
    image.save('converted_image.jpg')  # конвертация в формат JPEG
    image.save('converted_image.gif')  # конвертация в формат GIF
