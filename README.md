# Тестовое задание: API чатов и сообщений

REST API для чатов и сообщений на FastAPI с PostgreSQL.

## Стек технологий

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 (async)
- Alembic
- Pydantic v2

## Структура проекта

```
app/
├── main.py           # Точка входа
├── config.py         # Настройки
├── database.py       # Подключение к БД
├── models.py         # SQLAlchemy модели
├── schemas.py        # Pydantic схемы
├── crud.py           # Функции работы с БД
└── routes.py         # Эндпоинты
```

## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/innocentzy/test-chat-fastapi.git
cd test-chat-fastapi

# Создать .env файл
cp .env.example .env

# Запустить контейнеры
docker-compose up --build
```

API будет доступен по адресу: http://localhost:8000

Swagger UI: http://localhost:8000/docs

## API Endpoints

| Метод  | Endpoint              | Описание                                |
| ------ | --------------------- | --------------------------------------- |
| GET    | /chats/{id}?limit=N   | Получить чат и последние N сообщений    |
| POST   | /chats                | Создать чат                             |
| POST   | /chats/{id}/messages/ | Отправить сообщение в чат               |
| DELETE | /chats/{id}           | Удалить чат вместе со всеми сообщениями |

## Тестирование

```bash
# Установить зависимости для тестов
pip install -r requirements.txt

# Запустить тесты
pytest
```

## Переменные окружения

| Переменная   | Описание                     | По умолчанию                                            |
| ------------ | ---------------------------- | ------------------------------------------------------- |
| DATABASE_URL | URL подключения к PostgreSQL | postgresql+asyncpg://postgres:postgres@db:5432/testchat |

## Миграции

```bash
# Создать новую миграцию
alembic revision --autogenerate -m "description"

# Применить миграции
alembic upgrade head

# Откатить последнюю миграцию
alembic downgrade -1
```
