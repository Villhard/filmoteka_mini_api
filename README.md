# Filmoteka Mini API

## Описание
Простое API для организации библиотеки фильмов.
Позволяет создавать пользователей путем регистрации. Аутентификация пользователей происходит по обычному auth-токену.

## Основные возможности
### Пользователи
- `POST /auth/users/` - Регистрация пользователя (any user)
- `GET /auth/users/` - Получение списка пользователей (admin user)
- `GET /auth/users/me/` - Получение своего профиля (auth user)
- `GET /auth/users/{id}/` - Получение профиля пользователя (admin user)
- `PUT /auth/users/me/` - Редактирование своего профиля (auth user)
- `PUT /auth/users/{id}/` - Редактирование профиля пользователя (admin user)
- `DELETE /auth/users/me/` - Удаление своего профиля (auth user)
- `DELETE /auth/users/{id}/` - Удаление профиля пользователя (admin user)
- `POST /auth/token/login/` - Получение токена (any user, needs login and password)
- `POST /auth/token/refresh/` - Обновление токена (auth user)
- `POST /auth/token/logout/` - Удаление токена (auth user)

### Фильмы
- `GET /api/v1/films/` - Получение списка фильмов (any user)
- `POST /api/v1/films/` - Добавление фильма в библиотеку (admin user)
- `GET /api/v1/films/{id}/` - Получение информации о фильме (any user)
- `PUT /api/v1/films/{id}/` - Редактирование информации о фильме (admin user)
- `DELETE /api/v1/films/{id}/` - Удаление фильма из библиотеки (admin user)

### Избранное
- `GET /api/v1/favorite/` - Получение списка избранных фильмов (auth user)
- `POST /api/v1/films/{id}/favorite/` - Добавление фильма в избранное (auth user)
- `DELETE /api/v1/films/{id}/favorite/` - Удаление фильма из избранного (auth user)

## Технологии
- Django REST framework
- Djoser
- SQLite
