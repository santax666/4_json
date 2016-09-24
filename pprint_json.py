import json
import sys


def load_data(filepath):
    return json.load(open(filepath, 'r'))


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print("Скрипт выводит содержимое JSON-файла в удобном ввиде.")
            print("Введите в терминале: python3.5 pprint_json.py youfile.json")
        else:
            print(pretty_print_json(load_data(sys.argv[1])))
    else:
        print("Не задан файл для вывода!")
