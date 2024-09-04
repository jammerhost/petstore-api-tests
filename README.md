# tester-petstore
Автоматизированное тестирование API сайта Petstore с использованием Pytest.

Проект создан с учётом принципов объектно-ориентированного программирования (ООП)
и проходит проверку качества кода с помощью pylint с результатом 10/10

# Требования к запуску

* Python 3.10

# Работа с автотестами

Для выполнения тестов необходимо:

1. Открыть проект в IDE (например PyCharm/VSCode)
2. Создать venv (виртуальное окружение) с помощью команды `python -m venv venv`
3. Открыть новый терминал, убедиться в настроенном venv
4. Установить библиотеки с помощью команды `pip install -r requirements.txt`
5. Выполнить тесты командой `pytest`, либо, для генерации отчета выполнить `pytest --html=./result.html --self-contained-html`

В результате выполнения в корневой директории будет создан файл отчета

## Запуск отдельного файла тестирования
Для запуска конкретного теста выполнить команду с самим файлом, например `pytest tests/test_user.py`

# Пример логирования

В проекте реализована система логирования,
которая отслеживает выполнение всех ключевых шагов

Логи выводятся в консоль в процессе выполнения тестов,
что поможет отслеживать статус выполнения запросов и взаимодействий с API. Результат также выводится в отчет html

Пример логов:

```sql
2024-09-04 12:45:12,345 - test_user - INFO - Создание пользователя: user_1234
2024-09-04 12:45:12,567 - test_user - INFO - Пользователь user_1234 успешно создан
```
# Структура тестов

* tests/test_pet.py: Тесты для работы с питомцами (создание, получение, обновление и удаление питомцев).
* tests/test_user.py: Тесты для работы с пользователями (создание, получение, обновление и удаление пользователей).
