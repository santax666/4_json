import json


def load_data(filepath):
    return json.load(open(filepath, 'r'))


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)
# sort_keys - ключи выводимого словаря будут отсортированы
# ident - массивы и объекты в JSON будут выводиться с этим уровнем отступа
# ensure_ascii - строки запишутся как есть (без экранирования)

if __name__ == '__main__':
    print(pretty_print_json(load_data('alc.json')))
