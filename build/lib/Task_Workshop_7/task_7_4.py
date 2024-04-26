"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона."""

import random
import secrets
import string
from pathlib import Path

# Определение констант для значений по умолчанию
MIN_NAME_LENGTH = 6
MAX_NAME_LENGTH = 30
MIN_FILE_SIZE = 256  # Минимальный размер содержимого файла в символах
MAX_FILE_SIZE = 4096  # Максимальный размер содержимого файла в символах
FILE_COUNT = 42
BASE_DATA_PATH = Path('data_lesson_7')


def create_files(extension: str, min_name_length: int = MIN_NAME_LENGTH,
                 max_name_length: int = MAX_NAME_LENGTH, min_file_size: int = MIN_FILE_SIZE,
                 max_file_size: int = MAX_FILE_SIZE, file_count: int = FILE_COUNT) -> None:
    """
    Создает заданное количество файлов с случайными именами и содержимым.

    Параметры:
    extension (str): Расширение создаваемых файлов.
    min_name_length (int, optional): Минимальная длина имени файла. По умолчанию MIN_NAME_LENGTH.
    max_name_length (int, optional): Максимальная длина имени файла. По умолчанию MAX_NAME_LENGTH.
    min_file_size (int, optional): Минимальный размер содержимого файла в символах. По умолчанию MIN_FILE_SIZE.
    max_file_size (int, optional): Максимальный размер содержимого файла в символах. По умолчанию MAX_FILE_SIZE.
    file_count (int, optional): Количество создаваемых файлов. По умолчанию FILE_COUNT.

    Возвращает:
    None
    """
    BASE_DATA_PATH.mkdir(parents=True, exist_ok=True)
    for _ in range(file_count):
        # Генерация случайного имени файла
        file_name = ''.join(secrets.choice(string.ascii_lowercase) for _ in
                            range(random.randint(min_name_length, max_name_length))) + '.' + extension
        file_path = BASE_DATA_PATH / file_name
        # Генерация содержимого файла в виде текста
        file_content = ''.join(secrets.choice(string.ascii_letters + string.digits + ' ') for _ in
                               range(random.randint(min_file_size, max_file_size)))
        with file_path.open('w', encoding='utf-8') as file:
            file.write(file_content)


# Пример вызова функции для создания текстовых файлов
create_files('txt')
