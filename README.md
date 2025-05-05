
# Barter Platform — Платформа обмена вещами на Django

Веб-приложение, где пользователи могут размещать объявления и предлагать обмен на товары других пользователей.

---

## 🚀 Функциональность

- 🔐 Регистрация и вход пользователей (на основе Django)
- 📦 Создание, редактирование и удаление объявлений
- 🔎 Поиск и фильтрация по категории, названию и состоянию
- 🔁 Предложение обмена между пользователями
- ✅ Принятие или отклонение входящих предложений
- 👤 Раздел "Мои предложения" (входящие и исходящие)

---

## ⚙️ Установка и запуск

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/JustSterben/forwork.git
cd forwork
```

### 2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
venv\Scripts\activate      # Для Windows
# или
source venv/bin/activate  # Для macOS/Linux
```

### 3. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 4. Выполните миграции и создайте суперпользователя:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Запустите сервер:

```bash
python manage.py runserver
```

Перейдите в браузере: http://127.0.0.1:8000

---

## 🧪 Тестирование

```bash
python manage.py test
```

---

## 📁 Структура проекта

```
barter_test/
├── ads/                  # Приложение с объявлениями и обменами
├── barter_platform/      # Настройки проекта
├── templates/            # Шаблоны HTML
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📬 Контакты

Автор: [JustSterben](https://github.com/JustSterben)  
Почта: madaratver2@mail.ru
