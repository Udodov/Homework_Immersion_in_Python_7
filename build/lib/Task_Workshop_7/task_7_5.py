"""Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи."""

from typing import List, Dict

# Предполагаем, что функция create_files уже импортирована из task_7_4
from task_7_4 import create_files

# Константы для количества файлов каждого типа
TXT_FILE_COUNT = 5
LOG_FILE_COUNT = 3
CSV_FILE_COUNT = 7
MP4_FILE_COUNT = 2
MOV_FILE_COUNT = 2
AVI_FILE_COUNT = 1
JPG_FILE_COUNT = 4
JPEG_FILE_COUNT = 2
PNG_FILE_COUNT = 3
GIF_FILE_COUNT = 1
MP3_FILE_COUNT = 3
WAV_FILE_COUNT = 2
AAC_FILE_COUNT = 1


def create_files_with_extensions(extensions: List[str], files_count_by_extension: Dict[str, int]) -> None:
    """
    Генерирует файлы с разными расширениями в соответствии с указанным количеством для каждого расширения.

    Параметры:
    extensions (List[str]): Список расширений файлов.
    files_count_by_extension (Dict[str, int]): Словарь, где ключи - расширения файлов,
      а значения - количество файлов для создания.

    Возвращает:
    None
    """
    for extension in extensions:
        if extension in files_count_by_extension:
            create_files(extension, file_count=files_count_by_extension[extension])


# Пример использования с расширенным списком файлов
extensions_example = ['txt', 'log', 'csv', 'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png', 'gif', 'mp3', 'wav', 'aac']
files_count_by_extension_example = {
    'txt': TXT_FILE_COUNT,
    'log': LOG_FILE_COUNT,
    'csv': CSV_FILE_COUNT,
    'mp4': MP4_FILE_COUNT,
    'mov': MOV_FILE_COUNT,
    'avi': AVI_FILE_COUNT,
    'jpg': JPG_FILE_COUNT,
    'jpeg': JPEG_FILE_COUNT,
    'png': PNG_FILE_COUNT,
    'gif': GIF_FILE_COUNT,
    'mp3': MP3_FILE_COUNT,
    'wav': WAV_FILE_COUNT,
    'aac': AAC_FILE_COUNT
}

create_files_with_extensions(extensions_example, files_count_by_extension_example)
