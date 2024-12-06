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

## Установка
1. Клонировать репозиторий
```bash
git clone https://github.com/Villhard/filmoteka_mini_api.git
```
2. Перейти в папку проекта
```bash
cd filmoteka_mini_api
```
3. Создать виртуальное окружение
```bash
python -m venv venv
```
4. Активировать виртуальное окружение

Windows:
```bash
venv\Scripts\activate
```
Linux/MacOS:
```bash
source venv/bin/activate
```
5. Установить зависимости
```bash
pip install -r requirements.txt
```
6. Создать файл `.env` из шаблона `.env.example` и заполнить его данными
```bash
cp .env.example .env
```
7. Применить миграции
```bash
python manage.py migrate
```
8. Создать суперпользователя
```bash
python manage.py createsuperuser
```
9. Запустить сервер
```bash
python manage.py runserver
```