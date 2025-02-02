# Образовательный Telegram Бот по Фармакологии

Этот бот предназначен для обучения фармакологии через интерактивные уроки и тесты.

## Особенности

- 📚 Структурированные курсы по фармакологии
- ✍️ Интерактивные тесты после каждого урока
- 📊 Отслеживание прогресса обучения
- 🔒 Система доступа к урокам через код
- 🎯 Мгновенная обратная связь по результатам тестов

## Технологии

- Python 3.8+
- python-telegram-bot 20.7
- SQLAlchemy 2.0.25
- SQLite

## Установка и запуск

### Через Docker

```bash
# Сборка образа
docker build -t education-bot .

# Запуск контейнера
docker run -d --name education-bot education-bot
```

### Локальная установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/rinatuse/telegram.git
cd telegram
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Запустите бота:
```bash
python src/bot.py
```

## Структура проекта

```
education-bot/
├── src/
│   ├── bot.py          # Основной класс бота
│   ├── database.py     # Модели базы данных
│   └── demo_data.py    # Демонстрационные данные
├── requirements.txt    # Зависимости проекта
└── Dockerfile         # Конфигурация Docker
```

## Использование

1. Начните диалог с ботом командой `/start`
2. Выберите интересующий курс
3. Введите код доступа к уроку
4. Изучите материал
5. Пройдите тест командой `/test`

## Лицензия

MIT