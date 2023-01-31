import pandas as pd

def data_ ():
    df = pd.read_csv("data2.csv", delimiter=';')
    # Ложим значения в 'data'
    data = df.values
    my_list = []
    # Создаем словарь с ключами
    for i in range(len(data)):
            bibl = dict(zip(["ID", "NAME", "SALARY", "POSITION"], data[i]))
            my_list.append(bibl)
    return my_list




# def update_spreadsheet(path: str, _df, starcol: int = 1, startrow: int = 1, sheet_name: str = "ToUpdate"):
#     '''
#
#     :param path: Путь до файла Excel
#     :param _df: Датафрейм Pandas для записи
#     :param starcol: Стартовая колонка в таблице листа Excel, куда буду писать данные
#     :param startrow: Стартовая строка в таблице листа Excel, куда буду писать данные
#     :param sheet_name: Имя листа в таблице Excel, куда буду писать данные
#     :return:
#     '''
#     wb = ox.load_workbook(path)
#     for ir in range(0, len(_df)):
#         for ic in range(0, len(_df.iloc[ir])):
#             wb[sheet_name].cell(startrow + ir, starcol + ic).value = _df.iloc[ir][ic]
#     wb.save(path)
#
# xlsx_path = os.path.dirname(__file__) + r"\result.xlsx"
# update_spreadsheet(xlsx_path, df.sample(5), sheet_name = '1', starcol = 1, startrow =1)
