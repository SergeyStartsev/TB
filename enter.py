# Cделать импорт экспорт даты
# Cделать типорт импорт даты



def choice_todo():
ch = input("Введите цифру: ")
if ch == '1':
         sep = ' '                      #choice_sep()убрать
         import_data.import_data(input_data(), sep)
elif ch == '2':
    data = export_data2.read_csv_col
    print_data(data)
elif ch == '3':
    word = input("Введите данные для поиска: ")
    data = export_data2.read_csv_col()
    item = search_data(word, data)
    if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
    else:
            print("Данные не обнаружены")
    # else:
    #     word = input("Какой контакт надо удалить? ")
    #     data = export_data2()
    #     item = search_data(word, data)
    #     if item != None:
    #         print("Фамилия".center(20), "Имя".center(20), "Телефон".center(15), "Примечание".center(30))
    #         print("-"*85)
    #         del(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))# не знаю как сделать удаление