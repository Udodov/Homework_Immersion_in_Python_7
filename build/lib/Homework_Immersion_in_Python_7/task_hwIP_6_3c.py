""" - Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь
    - Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
* Добавить доп функционал. Чтобы программа возвращала список пар координат бьющих друг друга ферзей
(или пустой список, если ферзи не бьют друг друга).
** Модификация: выводить дополнительно одну расстановку, где ферзи бьют друг друга """

import random
from typing import List, Tuple

from task_hwIP_6_3b import BOARD_SIZE, is_safe, find_attacking_pairs


def find_queens_solutions() -> Tuple[List[Tuple[List[Tuple[int, int]],
                                                List[Tuple[Tuple[int, int], Tuple[int, int]]]]], List[Tuple[int, int]]]:
    """
    Генерация 4 успешных расстановок ферзей и одной расстановки с бьющими друг друга ферзями.
    """
    unique_solutions = []
    example_with_conflict = None  # Пример расстановки с конфликтами
    while len(unique_solutions) < 4 or not example_with_conflict:
        queens = [-1] * BOARD_SIZE
        for col in range(BOARD_SIZE):
            safe_positions = [r for r in range(BOARD_SIZE) if is_safe(r, col, queens)]
            if not safe_positions:
                break
            queens[col] = random.choice(safe_positions)
        current_attacking_pairs = find_attacking_pairs(queens)
        solution_as_tuples = [(col, queens[col]) for col in range(BOARD_SIZE)]
        if all(is_safe(r, col, queens) for col, r in enumerate(queens)):
            if solution_as_tuples not in unique_solutions:
                unique_solutions.append((solution_as_tuples, current_attacking_pairs))
        elif not example_with_conflict and current_attacking_pairs:
            example_with_conflict = solution_as_tuples  # Сохраняем первую найденную расстановку с конфликтами
    return unique_solutions, example_with_conflict


if __name__ == "__main__":
    random.seed()  # Инициализация генератора случайных чисел
    found_solutions, conflict_example = find_queens_solutions()
    for idx, (solution, attacking_pairs) in enumerate(found_solutions, 1):
        print(f"Расстановка #{idx}: {solution}")
        if attacking_pairs:
            print(f"Пары бьющих друг друга ферзей: {attacking_pairs}")
        else:
            print("Ферзи не бьют друг друга.")

    # Выводим пример расстановки с конфликтами
    if conflict_example:
        print("\nПример расстановки с бьющими друг друга ферзями (не удовлетворяет условиям задачи):")
        print(conflict_example)
        attacking_pairs_example = find_attacking_pairs([row for col, row in conflict_example])
        print(f"Пары бьющих друг друга ферзей: {attacking_pairs_example}")
