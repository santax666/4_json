import json


def load_data(filepath):
    return json.load(open(filepath,'r'))

def pretty_print_json(data):
    i = 0
    start_pos = 0
    print(data[0])
    print('')
    print(' '*start_pos,'[')
    start_pos = start_pos + 1
    print(' '*start_pos,'{')

    str_json = str(data[0])
#    str_json.find('{',0,len(str_json))
    print(str_json.find('{',0,len(str_json)))
#    while i < len(data):



if __name__ == '__main__':
    data = load_data('alc.json')
    pretty_print_json(data)

#        if data[i]["Cells"]["SeatsCount"] == data[max_seats]["Cells"]["SeatsCount"]:
#            sp_max.append(data[i]["Cells"]["Name"])
#        elif data[i]["Cells"]["SeatsCount"] > data[max_seats]["Cells"]["SeatsCount"]:
#            max_seats = i; sp_max = []; sp_max.append(data[i]["Cells"]["Name"]) #нашли больший бар, очищаем список больших баров
#        i = i + 1
#    return sp_max

