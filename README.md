# SVO Test Backend

Backend-приложение на FastAPI, обрабатывающее REST-запросы от фронтенда.

## Особенности

- FastAPI с CORS-мидлваром
- Подключённый роутер (`/routes/api.py`)
- Разрешён доступ с двух фронтов:
  - http://localhost:5173 (dev)
  - http://localhost:8080 (docker)
- Простая структура проекта
- Можно собирать и запускать в Docker

## Установка и запуск

### Локально

```bash
python -m venv venv
source venv/bin/activate  # или .\venv\Scripts\activate на Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Через Docker

```bash
docker build -t svo-backend .
docker run -d -p 8000:8000 --name svo-backend svo-backend
```

## API

Доступен по адресу: http://localhost:8000

Документация:
http://localhost:8000/docs
http://localhost:8000/redoc