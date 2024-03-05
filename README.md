# simple-api

## Доступные роуты

### 8 Ball

Возвращает случайный ответ "Магического шара".

```
/api/8ball
```

```json
{
    "answer": "ответ"
}
```

### isEven

Помогает определить, чётное ли число.

```
/api/is-even/:number
```

```json
{
    "isEven": true|false,
    "number": number
}
```

## Запуск в режиме разработки

```bash
flask --app app run --debug
```
