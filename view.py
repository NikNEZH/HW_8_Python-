import csv
import json
import model_2 as mod
dict = mod.data_()

def search_fo_name():
    a = input("NAME")
    for i in range(len(dict)):
        for key in dict[i]:
            if a == dict[i][key]:
                print(dict[i])

def search_fo_position():
    a = input("POSITION")
    ds_p = []
    for i in range(len(dict)):
        for key in dict[i]:
            if a == dict[i][key]:
                ds_p.append(dict[i])
                print(ds_p)

def search_fo_SALARY():
    a = int(input("SALARY"))
    ds_s = []
    for i in range(len(dict)):
        for key in dict[i]:
            if a == dict[i][key]:
                ds_s.append(dict[i])
                print(ds_s)

def write_data():
    print("Введите данные")
    id_str = int(input("Введите уникальный номер сотрудника (id): "))
    salary =input("Введите SALARY: ")
    name = input("Введите NAME: ")
    pos =input("Введите POSITION: ")
    d = [[id_str,name, salary, pos]]
    outfile = open('data2.csv', 'a')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    writer.writerows(d)
    outfile.close()

def write_upd():
    a = input("NAME")
    for i in range(len(dict)):
        for key in dict[i]:
            if a == dict[i][key]:
                print(dict[i])
                dict[i].update({
                                'NAME': input("NAME"),
                                'SALARY': int(input('Введите другую зп')),
                                'POSITION': input('Введите новую должность')})
                return dict

def write_data_csv():
    outfile = open('data2.csv', 'w')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    writer.writerows(dict)
    outfile.close()

def write_data_json():
    with open('data3.json', 'w') as outfile:
        json.dump(data, outfile)

def write_del():
    a = int(input("SALARY"))
    ds_del = []
    for i in range(len(dict)-1):
        for key in dict[i]:
            if a == dict[i][key]:
                dict.remove(dict[i])
                return dict