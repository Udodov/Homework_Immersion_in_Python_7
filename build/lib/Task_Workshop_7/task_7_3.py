"""Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало."""

from itertools import cycle
from pathlib import Path

BASE_DATA_PATH = Path('data_lesson_7')


def process_and_save_results(numbers_file: str, names_file: str, result_file: str) -> None:
    with open(BASE_DATA_PATH / numbers_file, 'r', encoding='utf-8') as nf, \
            open(BASE_DATA_PATH / names_file, 'r', encoding='utf-8') as names_f:
        # Измененная часть для обработки строк с числами
        numbers = [int(line.split('|')[0].strip()) for line in nf]
        names = [line.strip() for line in names_f]

        # Если один из файлов короче, используем cycle для бесконечного повторения его элементов
    max_len = max(len(numbers), len(names))
    numbers_cycle = cycle(numbers) if len(numbers) < max_len else numbers
    names_cycle = cycle(names) if len(names) < max_len else names

    with open(BASE_DATA_PATH / result_file, 'w', encoding='utf-8') as result_f:
        for number, name in zip(numbers_cycle, names_cycle):
            result = number * (names.index(name) + 1)  # Индекс имени + 1 для умножения
            result_line = f"{name.lower() if result < 0 else name.upper()} " \
                          f"{abs(result) if result < 0 else round(result)}\n"
            result_f.write(result_line)

        # Пример использования


process_and_save_results('random_pairs.txt', 'pseudonyms2.txt', 'result.txt')
