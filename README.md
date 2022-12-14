# Описание
## Модели:
1. Создана модель товара со следущими полями:
    - Название
    - Артикул
    - Цена
    - Статус
    - Изображение
2. Статус принимает одно из нескольких значений:
    - 1 - В наличии
    - 2 - Под заказ
    - 3 - Ожидается поступление
    - 4 - Нет в наличии
    - 5 - Не производится
## REST API точки:
1. списка товаров GET `http://localhost:8000/api/v1/products/`
2. информации о конретном товаре GET `http://localhost:8000/api/v1/products/id/`
3. добавить товар POST `http://localhost:8000/api/v1/products/`
    - {
    "title": "thirteen",
    "vendor_code": "111-1333",
    "price": "1212.12",
    "status": 3,
    "img": path_to_image
      } в form-data
     - реализован механизм конвертации изображения при загрузке из форматов PNG или JPG в формат WEBP.
4. Реализовано:
    - Фильтр по статусу `http://localhost:8000/api/v1/products/?status=1`
    - Поиск по артикулу и названию `http://localhost:8000/api/v1/products/?search=111-1333`
## Установка
1. Клонируйте репозиторий `git clone https://github.com/suband74/twrk-back`
2. Создайте виртуальное окружение `python3 -m venv env_twrk-back`
3. Активируйте виртуальное окружение `source env_twrk-back/bin/activate`
4. Установите зависимости `pip3 install -r requirements.txt`
5. Из папки с `twrk-back/shop` запустите проект `python3 manage.py runserver` 