"""Напишите функцию группового переименования файлов. Она должна:
    1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    2. принимать параметр количество цифр в порядковом номере.
    3. принимать параметр расширение исходного файла.
        Переименование должно работать только для этих файлов внутри каталога.
    4. принимать параметр расширение конечного файла.
    5. принимать диапазон сохраняемого оригинального имени.
        Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
        К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
* в одну строку"""

import glob
import os


def rename_files(target_name: str, num_digits: int, src_ext: str, dst_ext: str, name_range: tuple[int, int],
                 directory: str = ".") -> None:
    for idx, file in enumerate(glob.glob(f"{directory}/*.{src_ext}"), start=1):
        original_part = os.path.basename(file)[name_range[0]:name_range[1]]
        new_name = f"{original_part}{target_name}{str(idx).zfill(num_digits)}.{dst_ext}"
        os.rename(file, os.path.join(directory, new_name))

# Пример использования:
# rename_files("новое_имя", 3, "txt", "docx", (3, 6), "/путь/к/директории")
