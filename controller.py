import view as v

def show_menu() -> int:

    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    a = int(input("Введите номер необходимого действия: "))
    if a == 1:
        v.search_fo_name()
    elif a == 2:
        v.search_fo_position()
    elif a == 3:
        v.search_fo_SALARY()
    elif a == 4:
        v.write_data()
    elif a == 5:
        v.write_del()
    elif a == 6:
        v.write_upd()
    elif a == 7:
        v.write_data_csv()
    elif a == 8:
        v.write_data_json()
    elif a == 9:
        print("God bay!!")
