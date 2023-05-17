import mysql.connector as mc
from hash import make_password

def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        mysql_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(mysql_insert_query, record_to_insert)
        connection.commit()
    except (Exception, mc.Error) as error:
        print(error)

def connect():
    try:
        connection = mc.connect(user='root',host="localhost",password='joshua',database='PasswordManager')
        return connection
    except (Exception, mc.Error) as error:
        print(error)

def find_password(app_name):
    try:
        connection = connect()

        cursor = connection.cursor(buffered=True)
        mysql_select_query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(mysql_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' )
        print(result[0])
    
    except (Exception, mc.Error) as error:
        print(error)
        
def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ') 
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        mysql_select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(mysql_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('')
        print('-'*30)
    except (Exception, mc.Error) as error:
        print(error)

def update_password(app_name):
    try:
        email=input("Please enter the email: ")
        password = input("Enter the new password: ")
        new_password=make_password(password)
        connection=connect()
        mycursor = connection.cursor()
        sql = "UPDATE accounts SET password = %s WHERE email = %s AND app_name = %s"
        val = (new_password, email, app_name)
        mycursor.execute(sql, val)
        connection.commit()
        print(f"{mycursor.rowcount} record(s) affected")
    except (Exception, mc.Error) as error:
        print(error)


def delete_password(app_name):
    try:
        email=input("Please enter the email: ")
        connection=connect()
        mycursor = connection.cursor()
        sql = "DELETE FROM accounts WHERE email = %s AND app_name = %s"
        val = (email, app_name)
        mycursor.execute(sql, val)
        connection.commit()
        print(f"{mycursor.rowcount} record(s) affected")
    except (Exception, mc.Error) as error:
        print(error)

def show_all():
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ') 
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        mysql_select_query = " SELECT * FROM accounts "
        cursor.execute(mysql_select_query)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            print()
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('')
        print('-'*30)
    except (Exception, mc.Error) as error:
        print(error)

show_all()