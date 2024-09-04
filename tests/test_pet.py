"""
Тестирование части API питомцев
"""
# pylint: disable=redefined-outer-name

import pytest

from api.pet_api import PetAPI
from utils.assertions import assert_valid_schema
from utils.logger import setup_logger
from utils.schemas import pet_schema

# Инициализация логгера
logger = setup_logger()


# --------------------- FIXTURES ----------------------

@pytest.fixture(scope="module")
def pet_api():
    """
    Фикстура для работы с PetAPI
    """
    return PetAPI()


@pytest.fixture
def new_pet(pet_api):
    """
    Фикстура для создания питомца перед тестом и удаления после
    """
    pet_data = {
        "id": 123,
        "name": "Fluffy",
        "category": {"id": 1, "name": "Dogs"},
        "status": "available"
    }
    pet_api.create_pet(pet_data)
    yield pet_data
    pet_api.delete_pet(pet_data['id'])


# --------------------- TESTS ------------------------

@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_create_pet_with_different_statuses(pet_api, status):
    """
    Проверка создания питомца с разными статусами
    """
    pet_data = {
        "id": 124,
        "name": "TestPet",
        "category": {"id": 2, "name": "Cats"},
        "status": status
    }
    logger.info(f"Создание питомца со статусом: {status}")
    response = pet_api.create_pet(pet_data)
    assert response.status_code == 200, f"Failed to create pet with status: {status}"
    assert_valid_schema(response.json(), pet_schema)
    assert response.json()['status'] == status
    logger.info(f"Питомец со статусом {status} успешно создан")
    pet_api.delete_pet(pet_data['id'])


@pytest.mark.parametrize("pet_id, pet_name, category_id, category_name", [
    (125, "Doggo", 1, "Dogs"),
    (126, "Kitty", 2, "Cats"),
    (127, "Birdo", 3, "Birds")
])
def test_create_pet_with_various_data(pet_api, pet_id, pet_name, category_id, category_name):
    """
    Проверка создания питомцев с различными данными
    """
    pet_data = {
        "id": pet_id,
        "name": pet_name,
        "category": {"id": category_id, "name": category_name},
        "status": "available"
    }
    logger.info(f"Создание питомца: {pet_name} в категории {category_name}")
    response = pet_api.create_pet(pet_data)
    assert response.status_code == 200, f"Failed to create pet {pet_name}"
    assert_valid_schema(response.json(), pet_schema)
    assert response.json()['name'] == pet_name
    logger.info(f"Питомец {pet_name} успешно создан")
    pet_api.delete_pet(pet_data['id'])


@pytest.mark.parametrize("update_data", [
    {"name": "FluffyUpdated", "status": "sold"},
    {"name": "FluffySuper", "status": "pending"},
    {"name": "FluffyMax", "status": "available"}
])
def test_update_pet(pet_api, new_pet, update_data):
    """
    Параметризированный тест обновления данных питомца
    """
    updated_data = new_pet.copy()
    updated_data.update(update_data)
    logger.info(f"Обновление питомца с ID {new_pet['id']} новыми данными: {update_data}")

    response = pet_api.update_pet(updated_data)
    assert response.status_code == 200, "Pet update failed"
    assert_valid_schema(response.json(), pet_schema)
    assert response.json()['name'] == update_data["name"]
    assert response.json()['status'] == update_data["status"]
    logger.info(f"Питомец с ID {new_pet['id']} успешно обновлен: {update_data}")


@pytest.mark.parametrize("pet_id, pet_name, category_id, category_name", [
    (128, "DoggoToDelete", 1, "Dogs"),
    (129, "KittyToDelete", 2, "Cats"),
    (130, "BirdoToDelete", 3, "Birds")
])
def test_delete_pet(pet_api, pet_id, pet_name, category_id, category_name):
    """
    Параметризированный тест удаления питомцев
    """
    pet_data = {
        "id": pet_id,
        "name": pet_name,
        "category": {"id": category_id, "name": category_name},
        "status": "available"
    }
    logger.info(f"Создание питомца с ID {pet_id} для последующего удаления")
    pet_api.create_pet(pet_data)

    logger.info(f"Удаление питомца с ID {pet_id}")
    pet_api.delete_pet(pet_data['id'])

    response = pet_api.get_pet(pet_data['id'])
    assert response.status_code == 404, f"Pet with ID {pet_data['id']} was not deleted properly"
    logger.info(f"Питомец с ID {pet_id} успешно удален")
