"""
Класс взаимодействия с API petstore
"""
import requests


# pylint: disable=missing-timeout
class PetAPI:
    """
    Класс API
    """
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    # ---------------------- PET METHODS ----------------------

    def create_pet(self, pet_data):
        """
        Создание нового питомца

        :param pet_data: словарь с данными питомца
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.post(url, json=pet_data, headers=self.headers)
        return response

    def get_pet(self, pet_id):
        """
        Получение информации о питомце по его ID

        :param pet_id: ID питомца
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_pet(self, pet_data):
        """
        Обновление информации о питомце

        :param pet_data: словарь с обновленными данными питомца
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.put(url, json=pet_data, headers=self.headers)
        return response

    def delete_pet(self, pet_id):
        """
        Удаление питомца по его ID

        :param pet_id: ID питомца
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.delete(url, headers=self.headers)
        return response

    def find_pet_by_status(self, status):
        """
        Получение списка питомцев по статусу

        :param status: Статус питомца (available, pending, sold)
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet/findByStatus"
        params = {"status": status}
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def upload_pet_image(self, pet_id, image_path):
        """
        Загрузка изображения для питомца

        :param pet_id: ID питомца
        :param image_path: путь до файла изображения
        :return: объект response
        """
        url = f"{self.BASE_URL}/pet/{pet_id}/uploadImage"
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(url, headers={"accept": "application/json"}, files=files)

        return response

    # ---------------------- STORE METHODS ----------------------

    def get_inventory(self):
        """
        Получение информации о доступности товаров

        :return: объект response
        """
        url = f"{self.BASE_URL}/store/inventory"
        response = requests.get(url, headers=self.headers)
        return response

    def create_order(self, order_data):
        """
        Создание нового заказа

        :param order_data: словарь с данными заказа
        :return: объект response
        """
        url = f"{self.BASE_URL}/store/order"
        response = requests.post(url, json=order_data, headers=self.headers)
        return response

    def get_order(self, order_id):
        """
        Получение информации о заказе по его ID

        :param order_id: ID заказа
        :return: объект response
        """
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def delete_order(self, order_id):
        """
        Удаление заказа по его ID

        :param order_id: ID заказа
        :return: объект response
        """
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = requests.delete(url, headers=self.headers)
        return response

    # ---------------------- USER METHODS ----------------------

    def create_user(self, user_data):
        """
        Создание нового пользователя

        :param user_data: словарь с данными пользователя
        :return: объект response
        """
        url = f"{self.BASE_URL}/user"
        response = requests.post(url, json=user_data, headers=self.headers)
        return response

    def get_user(self, username):
        """
        Получение информации о пользователе по имени

        :param username: имя пользователя
        :return: объект response
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_user(self, username, user_data):
        """
        Обновление данных пользователя

        :param username: имя пользователя
        :param user_data: словарь с обновленными данными пользователя
        :return: объект response
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.put(url, json=user_data, headers=self.headers)
        return response

    def delete_user(self, username):
        """
        Удаление пользователя по имени

        :param username: имя пользователя
        :return: объект response
        """
        url = f"{self.BASE_URL}/user/{username}"
        response = requests.delete(url, headers=self.headers)
        return response
