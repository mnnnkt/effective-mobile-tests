## Описание проекта:

Данный проект представляет собой фреймворк для автоматизации тестирования с использованием следующих технологий:
Pytest - фреймворк для тестирования
Playwright - инструмент для автоматизации браузеров
Allure - система генерации красивых отчётов


Требования к окружению:

Python 3.10+
Java 8+ (требуется для Allure)


Установка зависимостей:

Установите необходимые пакеты Python:

pip install -r requirements.txt

Установите браузеры Playwright:

python -m playwright install

Установите Allure Report:

https://allurereport.org/docs/v2/install/

Проверка установки Allure:

Чтобы проверить корректность установки Allure, выполните:

allure --version


Запуск тестов:

Базовые команды

Запуск всех тестов:

pytest

Запуск тестов с определённым браузером:

pytest --browser=chromium

Запуск регрессионных тестов:

pytest -m regress

Запуск конкретного теста:

pytest tests/test_example.py::test_function


Генерация отчётов Allure:

Варианты генерации отчётов:

Запуск локального сервера:

allure serve allure-results

Генерация статического HTML отчёта:

allure generate allure-results -o allure-report


Запуск в docker:

Создание образа:

docker build -t my-test-framework .

Запускать контейнер нужно с пробросом порта:

docker run -p 5050:5050 -it my-test-framework bash

Тесты запускаются как обычно:

pytest

Генерировать отчёт нужно явно задавая хост и порт:

allure serve --host 0.0.0.0 --port 5050 allure-results

В таком случае страница с отчётом откроется извне по адресу http://localhost:5050


Конфигурация:

Основные настройки находятся в файле pytest.ini


Рекомендации по разработке:

Тестовые файлы должны начинаться с test_
Используйте маркеры для группировки тестов
Храните тесты в директории tests/


Поддержка и вопросы:

При возникновении вопросов обращайтесь к документации:
Pytest: https://docs.pytest.org
Playwright: https://playwright.dev/
Allure: https://allurereport.org/docs/







