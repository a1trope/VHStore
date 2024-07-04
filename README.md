## Кузнецов Александр, Тестовое задание Python

## Описание проекта
API сервис для интернет-магазина VHS-кассет. Список всех эндпоинтов лежит по **_api/swagger_**


## Доступ

Для большинства методов требуется авторизация. В качестве метода авторизации используется _TokenAuthetication_ из **Django REST Framework**.

#### 1. Запрос на регистрацию нового пользователя

POST: api/auth/signup

BODY:
```json
{
    "username": "rick",
    "password": "123"
}
```

_Ответ_:
```json
{
    "token": "...",
    "user": {
        "username": "jimmy",
        "password": "123"
    }
}
```

#### 2. Запрос на получение токена

BODY:
```json
{
    "username": "jimmy",
    "password": "123"
}
```

_Ответ_:
```json
{
    "token": "0d10ba79b691d17c69d6042369b8e013547476ef",
    "user": {
        "username": "jimmy",
        "password": "123"
    }
}
```





### Примеры Запросов

#### Модель:
```
class Cassette(models.Model):
    title: str
    director: str
    released: date (YYYY-MM-DD)
    quantity: uint
```

#### 1) GET: api/cassetes/

Статус ответа: 200 (OK)

_Ответ_:

```python
[
    {
        "id": 1,
        "title": "Jurassic Park",
        "director": "Steven Spielberg",
        "released": "1993-06-11",
        "quantity": 5
    },
    ...
]
```


#### 2) POST: api/cassetes/

Статус ответа: 201 (Created) и созданный объект

BODY:
```json
{
    "title": "Rambo",
    "director": "Ted Kotcheff",
    "released": "1992-10-22"
}
```

_Ответ_:
```json
{
    "id": 15,
    "title": "Rambo",
    "director": "Ted Kotcheff",
    "released": "1992-10-22",
    "quantity": 0
}
```


#### 3) PUT: api/cassetes/<id>

Статус ответа: 200 (OK)

BODY:

```json
{
    "title": "Rambo",
    "director": "Ted Kotcheff",
    "released": "1992-10-22",
    "quantity": 3
}
```


_Ответ_:
```json
{
    "id": 15,
    "title": "Rambo",
    "director": "Ted Kotcheff",
    "released": "1992-10-22",
    "quantity": 3
}
```



#### 4) PATCH: api/cassetes/<id>

Статус ответа: 204 (No content)

BODY:
```json
{
    "quantity": 3
}
```



#### 5) DELETE api/cassetes/<id>

Статус ответа: 204 (No content)