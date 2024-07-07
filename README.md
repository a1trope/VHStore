# Кузнецов Александр, Тестовое задание Python

# Содержание
- [Описание проекта](#-)
- [Доступ](#)
    - [1. Запрос на регистрацию нового пользователя](#1-----)
    - [2. Запрос на получение токена](#2----)
  - [Примеры Запросов](#-)
    - [Модель](#)
    - [1) GET: api/cassetes/](#1-get-apicassetes)
    - [2) POST: api/cassetes/](#2-post-apicassetes)
    - [3) PUT: api/cassetes/{id}](#3-put-apicassetesid)
    - [4) PATCH: api/cassetes/{id}](#4-patch-apicassetesid)
    - [5) DELETE api/cassetes/{id}](#5-delete-apicassetesid)


## Описание проекта
API сервис для интернет-магазина VHS-кассет. Список всех эндпоинтов лежит по **_api/swagger_**


## Доступ

Для всех запросов (кроме GET) требуется авторизация. В качестве метода авторизации используется _TokenAuthetication_ из **Django REST Framework**. Т.е. в заголовке к запросу нужно указать поле `Authorization: Token <token>` 

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
    "token": "...",
    "user": {
        "username": "jimmy",
        "password": "123"
    }
}
```

### Примеры Запросов

#### Модель
```python
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

Также можно отфильтровать список кассет, по всем полям (кроме `id`).
Например: `api/cassettes/?director=Steven Spielberg&quantity=5`
(получим кассеты Стивена Спилберга количество на складе которых равно 5-ти).


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


#### 3) PUT: api/cassetes/{id}

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



#### 4) PATCH: api/cassetes/{id}

Статус ответа: 204 (No content)

BODY:
```json
{
    "quantity": 3
}
```



#### 5) DELETE api/cassetes/{id}

Статус ответа: 204 (No content)
