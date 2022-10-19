import csv

def create_spravochnik(csv_file): #создать справочник
    with open(csv_file, 'w', newline='') as f:
        fieldnames= ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'id':'1', 'First_Name':'Ivan', 'Last_Name':'Ivanov','Number': '86326553333', 'Description': 'manager'})
        writer.writerow({'id':'2', 'First_Name':'Natalia', 'Last_Name':'Sergeva','Number': '9914553333', 'Description': 'cooker'})
        writer.writerow({'id':'3', 'First_Name':'Petr', 'Last_Name':'Ivanov','Number': '81272655323', 'Description': 'ingener'})


def read_spravochnik_add_new_cvsfile(new_csv_file, csv_file):  # добавление нового (csv) справочника в основной
    last_id=read_last_id()+1
    with open(new_csv_file, newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(csv_file, 'a', newline='') as csvfile_out:
            fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                writer.writerow({'id': last_id, 'First_Name': row['First_Name'], 
                    'Last_Name': row['Last_Name'], 'Number': row['Number'], 
                    'Description': row['Description']})
                last_id = last_id + 1

def read_last_id(): # Считывание последнего ID
    with open('phone.csv', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line[0].split(',')
        last_id = int(last_line[0])
        return last_id   

#read_spravochnik_add_new_cvsfile('phone.csv', 'phone1.csv')
    
