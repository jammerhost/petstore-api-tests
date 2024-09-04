"""
Настройки тестирования
"""


def pytest_html_report_title(report):
    """
    Задание заголовка отчета
    """
    report.title = "Отчет по автоматизированным тестам API PetStore"


def pytest_html_duration_format(duration):
    """
    Красивая подпись времени выполнения
    """
    if duration < 1:
        return f"{duration * 1000:.2f} ms"
    return f"{duration:.2f} s"
