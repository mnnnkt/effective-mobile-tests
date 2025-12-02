## Описание проекта:

### Данный проект представляет собой фреймворк для автоматизации тестирования с использованием следующих технологий:
* Pytest - фреймворк для тестирования
* Playwright - инструмент для автоматизации браузеров
* Allure - система генерации красивых отчётов


### Требования к окружению:
*Python 3.10+
*Java 8+ (требуется для Allure)


## Установка зависимостей:

### Установите необходимые пакеты Python:
```bash
pip install -r requirements.txt
```
### Установите браузеры Playwright:
```bash
python -m playwright install
```
### Установите Allure Report:

https://allurereport.org/docs/v2/install/

### Проверка установки Allure:

### Чтобы проверить корректность установки Allure, выполните:
```bash
allure --version
```

## Запуск тестов:

### Запуск всех тестов:
```bash
pytest
```
### Запуск тестов с определённым браузером:
```bash
pytest --browser=chromium
pytest --browser=firefox
pytest --browser=webkit
```
### Запуск регрессионных тестов:
```bash
pytest -m regress
```
### Запуск конкретного теста:
```bash
pytest tests/test_example.py::test_function
```

## Генерация отчётов Allure:

### Варианты генерации отчётов:

### Запуск локального сервера:
```bash
allure serve allure-results
```
### Генерация статического HTML отчёта:
```bash
allure generate allure-results -o allure-report
```

## Запуск в docker:

### Создание образа:
```bash
docker build -t my-test-framework .
```
### Запускать контейнер нужно с пробросом порта:
```bash
docker run -p 5050:5050 -it my-test-framework bash
```
### Тесты запускаются как обычно:
```bash
pytest
```
### Генерировать отчёт нужно явно задавая хост и порт:
```bash
allure serve --host 0.0.0.0 --port 5050 allure-results
```
### В таком случае страница с отчётом откроется извне по адресу http://localhost:5050


## Конфигурация:

Основные настройки находятся в файле pytest.ini


## Рекомендации по разработке:

* Тестовые файлы должны начинаться с test_
* Используйте маркеры для группировки тестов
* Храните тесты в директории tests/


## Поддержка и вопросы:

При возникновении вопросов обращайтесь к документации:
* Pytest: https://docs.pytest.org
* Playwright: https://playwright.dev/
* Allure: https://allurereport.org/docs/








