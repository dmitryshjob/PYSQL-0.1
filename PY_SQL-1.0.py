import psycopg2 
from pprint import pprint
# import pandas as pd


def delete_database():
    '''Удаление таблиц'''
    cur.execute("DROP TABLE client_phone,client CASCADE;")



def create_teble(): # БД (таблицы)
    '''Функция, создающая структуру БД (таблицы)'''

    cur.execute('''CREATE TABLE IF NOT EXISTS client(
        id SERIAL PRIMARY KEY,
        client_name VARCHAR (30) NOT NULL,
        client_surname VARCHAR(50) NOT NULL,
        client_email VARCHAR(150) NOT NULL,
        client_phone VARCHAR(20) )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS client_phone(
        id_phone SERIAL PRIMARY KEY,
        id_client INTEGER NOT NULL REFERENCES client(id),
        client_phone_number VARCHAR(20) NOT NULL)''')
    


def add_client(cur,client_phone_number = None): # добавить нового клиента
    '''Функция, позволяющая добавить нового клиента'''

    client_name = input('Введите имя клиента :')
    client_surname = input('Введите фамилию клиента :')
    client_email = input('Ввидите email клиента :')
    client_phone_number = input('Ввидите телефон клиента : ')

    cur.execute('''INSERT INTO client(
        client_name,client_surname,client_email,client_phone)
        VALUES(%s,%s,%s,%s);''',
        (client_name, client_surname, client_email, client_phone_number ))


def add_phone_number(cur): # добавить телефон для существующего клиента
    '''Функция, позволяющая добавить телефон для существующего клиента'''

    id_phone = input('Введите id клиента для добавления телефона :')
    phone_number = input('Введите номер :')
    cur.execute('''INSERT INTO client_phone(
        id_client, client_phone_number) VALUES(%s, %s)''',
        (id_phone, phone_number))


def changing_customer_information(): # изменить данные о клиенте
    '''Функция, позволяющая изменить данные о клиенте'''

    while True:
        print(" Чтобы измененить данные клиента, введите нужную команду.\n "
        "1 - изменить имя; 2 - изменить фамилию; 3 - изменить e-mail; 4 - изменить номер телефона \n "
        "Для просмотра таблицы нажмите -> '5'\n"
        " Или нажмите -> '6' для выхода из функции " )  

        while True:
            try:
                commands = int(input('Ввидите команду :'))
                break
            except ValueError:
                print('Вы ввели не число !!!')
        if commands == 6:
            break
        elif commands == 5:
            cur.execute('''SELECT *FROM client; ''')
            pprint(cur.fetchall())   
        elif commands == 1:
            id = input('Введите id клиента имя которого хотите изменить:')
            new_name = input('Введите имя клиента для изменения :')
            cur.execute(''' UPDATE client SET client_name=%s WHERE id=%s''',
            (new_name,id))

        elif commands == 2:   
            id = input('Введите id клиента фамилию которого хотите изменить:')  
            new_surname = input('Введите фамилию клиента для изменения :')
            cur.execute(''' UPDATE client SET client_surname=%s WHERE id=%s''',
            (new_surname, id))

        elif commands == 3:   
            id = input('Введите id клиента email которого хотите изменить:')  
            new_email = input('Введите email клиента для изменения :')
            cur.execute(''' UPDATE client SET client_email=%s WHERE id=%s''',
            (new_email, id))    

        elif commands == 4:   
            id = input('Введите id клиента телефон которого хотите изменить:')  
            new_phone = input('Введите телефон клиента для изменения :')
            cur.execute(''' UPDATE client SET client_phone_number=%s WHERE id=%s''',
            (new_phone, id))  
        else:
            print('\n Нет такой комнды !!! \n') 

def del_number(): # удалить телефон для существующего клиента
    '''Функция, позволяющая удалить телефон для существующего клиента''' 

    id_phone = input('Введите id клиента для удаления телефона :')
    cur.execute(''' DELETE FROM client_phone WHERE id_client=%s''',
    (id_phone))


def delete_client(): # Удалить клиента
    '''Функция, позволяющая удалить существующего клиен'''

    id_client = input('Введите id клиента для удаления всех данных :')   
    cur.execute(''' DELETE FROM client_phone WHERE id_client=%s''',
    (id_client)) 
    cur.execute(''' DELETE FROM client WHERE id=%s''',
    (id_client))  


def customer_search(): # Поиск клиентов
    '''Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)'''

    while True:
        print(" Чтобы найти данные клиента, введите нужную команду.\n "
        "1 - найти по имени; 2 - найти по фамилии; 3 - найти по e-mail; 4 - найти по номеру телефона \n "
        "Для просмотра таблицы нажмите -> '5'\n"
        " Или нажмите -> '6' для выхода из функции " )  

        while True:
            try:
                commands = int(input('Ввидите команду :'))
                break
            except ValueError:
                    print('Вы ввели не число !!!')
        if commands == 6:
            break
        elif commands == 5:
            cur.execute('''SELECT *FROM client; ''')
            pprint(cur.fetchall())  


        elif  commands == 1:
            name = input('Введите имя для поиска :')
            cur.execute(''' SELECT * FROM client
            JOIN client_phone ON client.id= client_phone.id_client 
            WHERE client_name=%s''',
            (name))
            pprint(cur.fetchall())

        elif  commands == 2:
            surname = input('Введите фамилию для поиска :')
            cur.execute(''' SELECT * FROM client
            JOIN client_phone ON client.id= client_phone.id_client 
            WHERE client_surname=%s''',
            (surname))
            pprint(cur.fetchall())

        elif  commands == 3:
            email = input('Введите email для поиска :')
            cur.execute(''' SELECT * FROM client
            JOIN client_phone ON client.id= client_phone.id_client 
            WHERE client_email=%s''',
            (email))
            pprint(cur.fetchall())

        elif  commands == 4:
            phone = input('Введите телефон для поиска :')
            cur.execute(''' SELECT * FROM client
            LEFT JOIN client_phone ON client.id = client_phone.id_client       
            WHERE client_phone_number = %s
             ''',
            (phone))
            pprint(cur.fetchall())  

        elif commands == 5:
            cur.execute('''SELECT * FROM client; ''')
            pprint(cur.fetchall())
           
            


if __name__=='__main__':


    with psycopg2.connect(database="customer_service", user="postgres", password="Az1111") as conn:
        
        print(" Управление структурой базы данных ")
        with conn.cursor() as cur:

            while True:
                print(" Введите число нужной команды.\n "
                "1 - Удалить таблицу\n 2 - Создать таблицу\n 3 - Добавить нового клиента\n 4 - Добавить телефон для существующего клиента \n "
                "5 - удалить телефон для существующего клиента\n 6 - Изменить данные о клиенте\n"
                " 7 - Удалить клиента\n 8 - Поиск клиентов \n")
  

               

                try:
                    commands = int(input('Ввидите команду :'))
                    break
                except ValueError:
                    print('Вы ввели не число !!!')

            if commands == 1:
                delete_database()
                print('Таблица удалена !!!')
                
            elif commands == 2:
                create_teble() # таблицы

                print("Таблица создана !!!")

            elif commands == 3:
                add_client(cur) # добавить нового клиента 
                print("Таблица клиентов ")
                cur.execute('''SELECT *FROM client; ''')  # ТАБЛИЦА client
                pprint(cur.fetchall()) 

            elif commands == 4:
                add_phone_number(cur) # добавить телефон для существующего клиента              
                cur.execute('''SELECT * FROM client
                LEFT JOIN client_phone ON client.id = client_phone.id_phone;''')
                pprint(cur.fetchall())  

            elif commands == 5:
                del_number() # удалить телефон для существующего клиента
                
            elif commands == 6:
                changing_customer_information() # изменить данные о клиенте

            elif commands == 7:   
                delete_client() # Удалить клиента 

            elif commands == 8: 
                customer_search() # Поиск клиентов

            else:
                print("Вы ввели неправильную команду, пожалуйста, повторите ввод")
 


        conn.close
    

