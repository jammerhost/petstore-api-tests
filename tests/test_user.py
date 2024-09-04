"""
Тестирование части API пользователей
"""

# pylint: disable=redefined-outer-name

import random
import pytest

from api.pet_api import PetAPI
from utils.logger import setup_logger

logger = setup_logger()


# --------------------- FIXTURES ----------------------

@pytest.fixture(scope="module")
def pet_api():
    """
    Фикстура для работы с PetAPI
    """
    return PetAPI()


@pytest.fixture
def new_user(pet_api):
    """
    Фикстура для создания пользователя перед тестом и удаления после
    """
    username = f"user_{random.randint(1000, 9999)}"
    user_data = {
        "id": random.randint(1, 1000),
        "username": username,
        "firstName": "John",
        "lastName": "Doe",
        "email": f"{username}@example.com",
        "password": "password123",
        "phone": "+1234567890",
        "userStatus": 1
    }
    response = pet_api.create_user(user_data)
    assert response.status_code == 200, "User creation failed"
    logger.info(f"Создан пользователь: {username}")
    yield user_data
    pet_api.delete_user(username)


# --------------------- TESTS ------------------------

def test_create_and_update_user(pet_api, new_user):
    """
    Создание пользователя, обновление данных и проверка всех шагов
    """
    username = new_user['username']

    # Шаг 1: Проверка создания пользователя
    logger.info(f"Проверка создания пользователя: {username}")
    response = pet_api.get_user(username)
    assert response.status_code == 200, f"User {username} not found"
    assert response.json()['username'] == username

    # Шаг 2: Обновление данных пользователя
    updated_data = new_user.copy()
    updated_data['firstName'] = "Jane"
    updated_data['lastName'] = "Smith"
    logger.info(f"Обновление пользователя {username}: firstName -> Jane, lastName -> Smith")
    response = pet_api.update_user(username, updated_data)
    assert response.status_code == 200, f"Failed to update user {username}"

    # Шаг 3: Проверка, что данные были обновлены
    logger.info(f"Проверка обновленных данных пользователя: {username}")
    response = pet_api.get_user(username)
    assert response.status_code == 200, f"User {username} not found after update"
    assert response.json()['firstName'] == "Jane"
    assert response.json()['lastName'] == "Smith"

    # Шаг 4: Удаление пользователя и проверка, что его больше нет
    logger.info(f"Удаление пользователя: {username}")
    response = pet_api.delete_user(username)
    assert response.status_code == 200, f"Failed to delete user {username}"

    response = pet_api.get_user(username)
    assert response.status_code == 404, f"User {username} still exists after deletion"


def test_create_duplicate_user(pet_api, new_user):
    """
    Проверка обработки ошибки при попытке создать дублирующего пользователя
    """
    logger.info(f"Попытка создать дублирующего пользователя: {new_user['username']}")

    # Создание пользователя
    _ = pet_api.create_user(new_user)

    # Попытка повторно создать того же пользователя
    response = pet_api.create_user(new_user)
    assert response.status_code == 400, "API did not return error for duplicate user creation"
    logger.info("API успешно вернуло ошибку при создании дублирующего пользователя")


def test_concurrent_user_updates(pet_api, new_user):
    """
    Одновременное обновление данных пользователя
    """
    username = new_user['username']

    # Определяем данные для двух разных обновлений
    update_data_1 = new_user.copy()
    update_data_1['firstName'] = "Concurrent_1"
    update_data_2 = new_user.copy()
    update_data_2['firstName'] = "Concurrent_2"

    logger.info(f"Конкурентное обновление пользователя {username}: 2 обновления одновременно")

    # Выполняем два одновременных обновления
    response_1 = pet_api.update_user(username, update_data_1)
    response_2 = pet_api.update_user(username, update_data_2)

    assert response_1.status_code == 200, "First concurrent update failed"
    assert response_2.status_code == 200, "Second concurrent update failed"

    # Проверяем, какое обновление было успешным в итоге
    final_response = pet_api.get_user(username)
    assert final_response.status_code == 200, f"User {username} not found after concurrent updates"
    logger.info(f"Результат конкурентного обновления: {final_response.json()['firstName']}")


def test_invalid_user_retrieval(pet_api):
    """
    Получение несуществующего пользователя
    """
    invalid_username = "non_existing_user"
    logger.info(f"Проверка получения несуществующего пользователя: {invalid_username}")
    response = pet_api.get_user(invalid_username)
    assert response.status_code == 404, "API did not return 404 for non-existing user"
    logger.info(f"API успешно вернуло ошибку для несуществующего пользователя: {invalid_username}")
