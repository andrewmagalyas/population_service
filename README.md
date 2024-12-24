# Population Data Service

Цей проект надає API сервіс для завантаження, збереження та виведення даних про населення країн. Використовується FastAPI, SQLAlchemy та PostgreSQL. Проект запускається через Docker Compose.

## Вміст

- [Встановлення та запуск](#встановлення-та-запуск)
- [Використання](#використання)
- [Структура проекту](#структура-проекту)
- [Додаткові налаштування](#додаткові-налаштування)

## Встановлення та запуск

### 1. Клонування репозиторію

```sh
    git clone https://github.com/andrewmagalyas/population_service.git
    cd population_service/
```
### 2. Запуск Docker Compose
Переконайтеся, що у вас встановлені Docker та Docker Compose. Далі запустіть наступні команди:
```sh
  docker-compose up -d
```
Це підніме контейнери з базою даних та додатком.

### 3. Завантаження даних
```shell
  docker-compose up get_data
```

### 4. Виведення агрегованих даних
```shell
  docker-compose up print_data
```

### Використання
- get_data: Завантажує, парсить і зберігає дані в базу.

- print_data: Читає дані з бази та виводить агреговані дані по регіонах.

### Структура проекту
```
population_service/
├── app/
│   ├── routers/
│   │   ├── data_router.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── get_data.py
│   ├── print_data.py
│   └── config.py
├── migrations/
│   └── versions
│   └── README
├── README.md
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
```

#### app/: Містить код додатку.

- __init__.py: Ініціалізація пакету.

- main.py: Основний файл FastAPI додатку.

- models.py: Моделі бази даних.

- database.py: Конфігурація бази даних.

- get_data.py: Скрипт для завантаження та збереження даних.

- print_data.py: Скрипт для виведення агрегованих даних.

- docker-compose.yml: Конфігурація Docker Compose.

#### Dockerfile: Опис Docker образу.

#### requirements.txt: Список залежностей.

#### README.md: Документація проекту.

### Додаткові налаштування
Файл .env для налаштування змінних оточення:

```plaintext
DATABASE_URL=postgresql://user:password@postgres/population_db
SOURCE_URL=https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959
```

Звісно, якщо вам потрібна будь-яка інша допомога чи додаткові пояснення, дайте знати!

```
andrewmagalyas@gmail.com
```
