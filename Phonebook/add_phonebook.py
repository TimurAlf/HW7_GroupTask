import csv
from add_contact import read_last_id

def add_new_directory(file_csv): # Добавление нового справочника
    with open(file_csv, 'w', newline='') as csvfile:
        fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id': '1', 'First_Name': 'Ivan', 
            'Last_Name': 'Ivanov', 'Number': '89991234567', 'Description': 'Teacher'})
        writer.writerow({'id': '2', 'First_Name': 'Petr', 
            'Last_Name': 'Petrov', 'Number': '89993234567', 'Description': 'Director'})
        writer.writerow({'id': '3', 'First_Name': 'Sergei', 
            'Last_Name': 'Sidorov', 'Number': '89995234567', 'Description': 'HomeWorker'})

def import_new_dir_at_directory(file_csv_new, file_csv): # Импортирование нового справочника(csv файл) в основной справочник
    last_id = read_last_id() + 1
    with open(file_csv_new, newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                writer.writerow({'id': last_id, 'First_Name': row['First_Name'], 
                    'Last_Name': row['Last_Name'], 'Number': row['Number'], 
                    'Description': row['Description']})
                last_id = last_id + 1