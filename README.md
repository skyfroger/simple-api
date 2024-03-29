# Simple API

## Размещение API в облаке

Для размещения собственной копии API можно использовать сервис [render.com](https://render.com). Создайте аккаунт на сервисе и нажмите следующую кнопку, чтобы автоматически создать веб-сервис.

[![Разместить на Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/skyfroger/simple-api)

Доступ к документации можно получить по адресу:

```
https://БАЗОВЫЙ_URL/docs
```

или

```
https://БАЗОВЫЙ_URL/redoc
```

## Доступные API

### 8 Ball

Возвращает случайный ответ "Магического шара".

### Число чётное?

Помогает определить, чётное ли число.

### Холст

Хранение координат и цвета точки на общем холсте.

### QR-код

Создание qr кода по заданному тексту.

## Запуск в режиме разработки

Установка необходимых модулей:

```bash
pip install -r requirements.txt
```

Запуск сервера разработки:

```bash
uvicorn main:app --reload
```
