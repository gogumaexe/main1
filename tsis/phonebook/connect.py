import psycopg2

def connection():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="max",
        password=""
    )