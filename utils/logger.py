"""
Настройка логгера
"""
import logging


def setup_logger():
    """
    Настройка логгера для использования в тестах с выводом в консоль.
    """
    # Создаем логгер
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Создаем обработчик вывода в консоль (StreamHandler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    if not logger.hasHandlers():  # Проверяем, чтобы не добавить обработчик несколько раз
        logger.addHandler(console_handler)

    return logger
