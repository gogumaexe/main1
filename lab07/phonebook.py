import psycopg2
import csv
from connect import get_db_connection

def insert_from_csv(file_path):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO contacts (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    
    conn.commit()
    cursor.close()
    conn.close()

def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (username, phone) VALUES (%s, %s)", (username, phone))
    
    conn.commit()
    cursor.close()
    conn.close()

def update_contact():
    contact_id = input("Enter contact ID to update: ")
    new_phone = input("Enter new phone number: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, contact_id))
    
    conn.commit()
    cursor.close()
    conn.close()

def query_contacts():
    filter_type = input("Filter by (name/phone prefix): ")
    filter_value = input("Enter value to filter by: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    if filter_type == "name":
        cursor.execute("SELECT * FROM contacts WHERE username LIKE %s", ('%' + filter_value + '%',))
    elif filter_type == "phone":
        cursor.execute("SELECT * FROM contacts WHERE phone LIKE %s", ('%' + filter_value + '%',))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()

def delete_contact():
    contact_id = input("Enter contact ID to delete: ")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    
    conn.commit()
    cursor.close()
    conn.close()