def write_txt_cols(phone_numbers):
    with open('phone_note.txt', 'w', encoding='utf-8', newline='') as file:
        for key in phone_numbers.keys():
            file.write(f'{key},\n{phone_numbers[key][0]}\n{phone_numbers[key][1]}\n{phone_numbers[key][2]}\n\n')

def write_csv_cols(phone_numbers):
    with open('phone_note.csv', 'w', encoding='utf-8', newline='') as file:
        for key in phone_numbers.keys():
            #ниже описывается как записать в файл. \n - это новая строка  key
            file.write(f'{key},\n{phone_numbers[key][0]}\n{phone_numbers[key][1]}\n{phone_numbers[key][2]}\n\n')

def read_txt_col():
    with open('phone_note.txt', 'r', encoding='utf-8', newline='') as file:
        readfile = file.read()
        tablo = ("".join(readfile))
        print(tablo)

#читает файл сиэсви столбиками
def read_csv_col():
    with open('phone_note.csv', 'r', encoding='utf-8', newline='') as file:
        readfile = file.read()
        tablo = ("".join(readfile))
        print(tablo)


def print_csv(phone_numbers):
    for key in phone_numbers.keys():
        tmp = phone_numbers[key]
        s = "".join(tmp)
        s = s.replace(',', ' ').replace("'","")
        print(f'{key} {s}')  # на выходе ключ со словаря и значения в виде строки


print_csv(type(read_csv_col))
# write_csv_cols(phone_numbers)
# read_csv_col()
# read_txt_col()