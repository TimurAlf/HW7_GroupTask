#Вывод справочника на экран.
def displaying_the_phone_directory_on_the_screen(file_csv):
    with open(file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['First_Name'], row['Last_Name'], 
            row['Number'], row['Description'])

#Считывание последнего id.
def reading_the_last_id():
    with open('telephon.csv', newline='') as csvfile:
        lastLine = csvfile.readlines()[-1]
        lastLine = lastLine[0].split(',')
        lastID = int(lastLine[0])
        return lastID

#Экспорт справочника
def export_phone_directory_text(file_txt):
    with open('telephon.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            with open(file_txt, 'a') as txtfile:
                stroka = ''
                stroka = str(row)
                txtfile.write(f'{stroka}\n')
