""" - Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь
    - Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
* Добавить доп функционал. Чтобы программа возвращала список пар координат бьющих друг друга ферзей
(или пустой список, если ферзи не бьют друг друга)."""

import random
from typing import List, Tuple

BOARD_SIZE = 8  # Размер шахматной доски


def is_safe(row: int, col: int, queens: List[int]) -> bool:
    """
    Проверка, безопасно ли разместить ферзя в данной позиции.
    """
    for prev_col in range(col):
        if queens[prev_col] == row or \
                queens[prev_col] - prev_col == row - col or \
                queens[prev_col] + prev_col == row + col:
            return False
    return True


def find_attacking_pairs(queens: List[int]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Находит пары бьющих друг друга ферзей.
    """
    pairs = []  # Используем уникальное имя для избежания затенения
    for col1 in range(BOARD_SIZE):
        for col2 in range(col1 + 1, BOARD_SIZE):
            row1 = queens[col1]
            row2 = queens[col2]
            if row1 == row2 or \
                    abs(row1 - row2) == abs(col1 - col2):
                pairs.append(((col1, row1), (col2, row2)))
    return pairs


def find_queens_solutions() -> List[Tuple[List[Tuple[int, int]], List[Tuple[Tuple[int, int], Tuple[int, int]]]]]:
    """
    Генерация 4 успешных расстановок ферзей и список пар координат бьющих друг друга ферзей.
    """
    unique_solutions = []
    while len(unique_solutions) < 4:
        queens = [-1] * BOARD_SIZE
        for col in range(BOARD_SIZE):
            safe_positions = [r for r in range(BOARD_SIZE) if is_safe(r, col, queens)]
            if not safe_positions:
                break
            queens[col] = random.choice(safe_positions)
        if all(is_safe(r, col, queens) for col, r in enumerate(queens)):
            solution_as_tuples = [(col, queens[col]) for col in range(BOARD_SIZE)]
            current_attacking_pairs = find_attacking_pairs(queens)
            if solution_as_tuples not in unique_solutions:
                unique_solutions.append((solution_as_tuples, current_attacking_pairs))
    return unique_solutions


if __name__ == "__main__":
    random.seed()  # Инициализация генератора случайных чисел
    found_solutions = find_queens_solutions()
    for idx, (solution, attacking_pairs) in enumerate(found_solutions, 1):
        print(f"Расстановка #{idx}: {solution}")
        if attacking_pairs:
            print(f"Пары бьющих друг друга ферзей: {attacking_pairs}")
        else:
            print("Ферзи не бьют друг друга.")
