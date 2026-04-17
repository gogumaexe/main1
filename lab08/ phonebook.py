import psycopg2
from config import DATABASE_CONFIG

def connect():
    try:
        connection = psycopg2.connect(
            dbname=DATABASE_CONFIG["dbname"],
            user=DATABASE_CONFIG["user"],
            password=DATABASE_CONFIG["password"],
            host=DATABASE_CONFIG["host"],
            port=DATABASE_CONFIG["port"]
        )
        return connection
    except Exception as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def execute_query(query, params=None):
    connection = connect()
    if connection is None:
        return None

    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        connection.rollback()
        return None
    finally:
        cursor.close()
        connection.close()

def execute_function(function_name, params=None):
    query = f"SELECT {function_name}({', '.join(['%s' for _ in params])})"
    return execute_query(query, params)

def execute_procedure(procedure_name, params=None):
    query = f"CALL {procedure_name}({', '.join(['%s' for _ in params])})"
    return execute_query(query, params)