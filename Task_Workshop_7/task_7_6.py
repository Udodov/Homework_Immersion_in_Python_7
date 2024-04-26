"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

from pathlib import Path
from typing import Dict, List

# Определение базового пути
BASE_DATA_PATH = Path('data_lesson_7')


def sort_files_to_directories(base_path: Path, extensions_mapping: Dict[str, List[str]]) -> None:
    """
    Сортирует файлы по директориям на основе их расширений.

    Параметры:
    base_path (Path): Базовый путь к директории с данными.
    extensions_mapping (Dict[str, List[str]]): Словарь, сопоставляющий директории с расширениями файлов.
    """
    for file in base_path.iterdir():
        if file.is_file():
            destination_dir = next(
                (base_path / dir_name for dir_name, exts in extensions_mapping.items() if file.suffix in exts), None)
            if destination_dir:
                destination_dir.mkdir(parents=True, exist_ok=True)
                file.rename(destination_dir / file.name)


# Расширенный пример использования с музыкой
extensions_mapping_example = {
    'videos': ['.mp4', '.mov', '.avi'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'texts': ['.txt', '.log', '.csv'],
    'music': ['.mp3', '.wav', '.aac']
}

sort_files_to_directories(BASE_DATA_PATH, extensions_mapping_example)
