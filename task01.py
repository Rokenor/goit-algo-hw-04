import argparse
import shutil
from pathlib import Path
import sys

def copy_and_sort_files(source_path: Path, dest_path: Path):
    ''' Рекурсивно копіює та сортує файли з вихідної директорії до директорії призначення'''
    
    try:
        # Перебираємо всі елемменти у вихідній директорії
        for item in source_path.iterdir():
            if item.is_dir():
                print(f"Обробляємо директорію: {item}")
                copy_and_sort_files(item, dest_path)
            elif item.is_file():
                # Визначаємо розширення файлу
                extension = item.suffix[1:] if item.suffix else "no_extension"

                # Створюємо шлях до піддиректорії на основі розширення
                target_dir = dest_path / extension
                    
                # Створюємо піддиректорію, якщо вона не існує
                target_dir.mkdir(parents=True, exist_ok=True)

                # Копіюємо файл
                shutil.copy2(item, target_dir)
                print(f"Скопійовано файл '{item.name}' до '{target_dir}'")

    except PermissionError:
        print(f"Немає доступу до директорії {source_path}")
    except Exception as e:
        print(f"Сталася невидома помилка при обробці {source_path}: {e}")

def main():
    '''Головна функція для парсингу аргументів та запуску процесу'''

    # Парсимо аргумети командного рядка
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює та сортує файли за розширеннями."
    )
    parser.add_argument(
        "source", 
        type=Path, 
        help="Шлях до вихідної директорії"
    )
    parser.add_argument(
        "-d", "--destination", 
        type=Path, 
        default=Path("dist"), 
        help="Шлях до директорії призначення (за замовчуванням: 'dist')"
    )

    args = parser.parse_args()

    source_dir = args.source
    dest_dir = args.destination

    # Перевірка, чи існує вихідна директорія
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Помилка: Вихідна директорія '{source_dir}' не існує або не є директорією.")
        sys.exit(1)

    print(f"Вихідна директорія: {source_dir}")
    print(f"Директорія призначення: {dest_dir}")

    # Запуск рекурсивної функції
    copy_and_sort_files(source_dir, dest_dir)
    print("\nЗавершено!")

if __name__ == "__main__":
    main()