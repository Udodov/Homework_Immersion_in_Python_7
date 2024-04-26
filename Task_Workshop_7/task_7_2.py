"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраняйте в файл."""

import string
from pathlib import Path
from random import choice, randint

BASE_DATA_PATH = Path('data_lesson_7')


def generate_pseudonym() -> str:
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    return ''.join(choice(consonants if i % 2 == 0 else vowels) for i in range(randint(4, 7))).capitalize()


def save_pseudonym_to_file(filename: str = 'pseudonyms.txt') -> None:
    pseudonym = generate_pseudonym()
    with (BASE_DATA_PATH / filename).open('a') as file:
        file.write(pseudonym + '\n')


# Убедитесь, что директория существует
BASE_DATA_PATH.mkdir(parents=True, exist_ok=True)

# Пример использования
save_pseudonym_to_file()
