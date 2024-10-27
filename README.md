 # Телеграмм бот для it-академии

## Описание

Это Telegram-бот, который помогает пользователям выбрать направление обучения и курсы, которые подходя его интересам.

## Технологический стек

- Python (3.12)
- aiogram (для работы с Telegram API)
- psycopg2 (для работы с PostgreSQL)
- Poetry (для управления зависимостями)


## Как запустить проект

1. Клонируйте репозиторий:

   git clone https://github.com/Gapenysh/Techno_Ed.git
    

2. Инициализируйте Poetry:

    
   poetry install
    

3. В файле .env добавьте необходимые переменные окружения вида:

DB_NAME=
USER=
PASSWORD=
HOST=
BOT_TOKEN=
CLIENT_ID=
GIGACHAT_API=
AUTH_KEY=


4. Запустите бота через файл main:

run python main.py

## Команда авторов

- Инсаф Ахметзянов 
- Булат Хайруллин
- Рамзиль Абдуллин 

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

