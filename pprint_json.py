import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Скрипт выводит содержимое JSON-файла в удобном ввиде.")
            print("Введите в терминале: python3.5 pprint_json.py youfile.json")
        else:
            json_file = load_data(sys.argv[1])
            if json_file is None:
                print("JSON-файл не обнаружен!")
            else:
                print(pretty_print_json(json_file))
    else:
        print("Не задан файл для вывода!")
