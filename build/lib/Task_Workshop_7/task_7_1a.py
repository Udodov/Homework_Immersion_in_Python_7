"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число — -1000, максимальное — +1000.
Количество строк и имя файла передаются как аргументы функции."""

from pathlib import Path
import random

MIN_INT: int = -1000  # Минимальное значение для int
MAX_INT: int = 1000  # Максимальное значение для int

# Определим базовый путь к директории с данными
BASE_DATA_PATH = Path('data_lesson_7')
output_file_path = BASE_DATA_PATH / 'random_pairs2.txt'


def append_random_pairs_to_file(target_file_path: Path, lines_count: int) -> None:
    """
    Добавляет в файл случайные пары чисел: целое и вещественное.

    :param target_file_path: Путь к файлу, в который будут добавлены данные.
    :param lines_count: Количество строк для добавления.
    """

    # Убедимся, что директория, в которую мы хотим записать файл, существует.
    # Если нет, создадим её.
    target_file_path.parent.mkdir(parents=True, exist_ok=True)

    with target_file_path.open('a', encoding='utf-8') as file:
        for _ in range(lines_count):
            int_part: int = random.randint(MIN_INT, MAX_INT)
            float_part: float = random.uniform(MIN_INT, MAX_INT)
            file.write(f"{int_part}|{float_part:.2f}\n")


# Пример использования функции:
example_lines_count: int = 10

append_random_pairs_to_file(output_file_path, example_lines_count)
