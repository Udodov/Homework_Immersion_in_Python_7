"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число — -1000, максимальное — +1000.
Количество строк и имя файла передаются как аргументы функции."""

import os
import random

MIN_INT: int = -1000  # Минимальное значение для int
MAX_INT: int = 1000  # Максимальное значение для int

# Определим базовый путь к директории с данными
BASE_DATA_PATH = 'data_lesson_7'
path_txt = os.path.join(BASE_DATA_PATH, 'random_pairs.txt')


def append_random_pairs_to_file(file_path: str, lines_count: int) -> None:
    """
    Добавляет в файл случайные пары чисел: целое и вещественное.

    :param file_path: Путь к файлу, в который будут добавлены данные.
    :param lines_count: Количество строк для добавления.
    """

    # Убедимся, что директория, в которую мы хотим записать файл, существует.
    # Если нет, создадим её.
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'a', encoding='utf-8') as file:
        for _ in range(lines_count):
            int_part: int = random.randint(MIN_INT, MAX_INT)
            float_part: float = random.uniform(MIN_INT, MAX_INT)
            file.write(f"{int_part}|{float_part:.2f}\n")


# Пример использования функции:
example_lines_count: int = 10

append_random_pairs_to_file(path_txt, example_lines_count)
