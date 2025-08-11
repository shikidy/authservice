# AuthService
Выполнено в рамках тестового задания.

## Deploy
```
git clone https://github.com/shikidy/authservice
```
Переименовываем example.env в .env и заполняем.

### Ручками (postgres установлена)
```
uv run uvicorn app:app --port 8000 --host 127.0.0.1
```

### Docker
```
docker-compose up
```

## Тестирование (postgres установлен)
```
uv run pytest
```
<img width="311" height="88" alt="image" src="https://github.com/user-attachments/assets/ddc4fb78-147b-4f2b-aa47-0e7fbd62c163" />

