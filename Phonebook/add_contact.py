import csv
import os
from os import system

def add_new_contact_in_phonebook(new_contact): # Добавление нового контакта не из csv
    last_id = read_last_id() + 1
    with open('telephone.csv', 'a', newline='') as csvfile_out:
        fieldnames = ['id', 'First_Name', 'Last_Name', 'Number', 'Description']
        writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
        writer.writerow({'id': last_id, 'First_Name': new_contact[0], 
                'Last_Name': new_contact[1], 'Number': new_contact[2], 
                'Description': new_contact[3]})


def import_phonebook_txt_file(file_txt): # Добавление контактов из txt файла
    with open(file_txt, 'r') as file:
        count = 0
        new_contact = []
        lines = file.readlines()
        for line in lines:
            if line.strip() == '':
                count = count
            else:
                new_contact.append(line.strip())
                count = count + 1          
            if count == 4:
                add_new_contact_in_phonebook(new_contact)
                count = 0
                new_contact = []
            else:
                continue

def new_contact_keyboard_input(): # ДОбавление нового контакта с клавиатуры
    print('Введите с клавиатуры')
    a = ['Имя: ','Фамилия: ','Номер: ','Описание: ']
    new_contact = []
    for i in range(4):
        new_contact.append(str(input(a[i])))
    add_new_contact_in_phonebook(new_contact)

def read_last_id(): # Считывание последнего ID
    with open('telephone.csv', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_id = int(last_line.split(',')[0])
    return last_id



file_txt = input('Введите файл *.txt > ')
import_phonebook_txt_file(file_txt)
new_contact_keyboard_input()
add_new_contact_in_phonebook()

        
   