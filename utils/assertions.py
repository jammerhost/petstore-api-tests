"""
Универсальная проверка данных
"""
from jsonschema.validators import validate


def assert_valid_schema(response_data, schema):
    """
    Проверяет соответствие ответа API заданной схеме.
    """
    validate(instance=response_data, schema=schema)


def assert_response_time(response, max_time=1.0):
    """
    Проверяет, что время выполнения запроса меньше заданного значения.
    """
    elapsed_time = response.elapsed.total_seconds()
    assert elapsed_time < max_time, f"Response took too long: {elapsed_time} seconds"
