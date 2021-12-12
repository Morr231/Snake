import sqlite3
from sqlite3 import OperationalError, Row
from contextlib import contextmanager


@contextmanager
def new_connection():
    connection = sqlite3.connect('users.db')

    try:
        yield connection
    finally:
        if connection:
            connection.close()


def create_table():
    with new_connection() as connect:
        try:
            cursor = connect.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(40) NOT NULL,
                    score VARCHAR(10) NOT NULL
                );
            """)
        except OperationalError as err:
            print(f'\n {err}')


def add_user_on_table(name, score):
    with new_connection() as connect:
        try:
            connect.row_factory = Row
            cursor = connect.cursor()
            cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
            user = cursor.fetchall()
            if len(user) == 0:
                cursor.execute("""
                    INSERT INTO users
                        (name, score)
                    VALUES
                        (?, ?)""", (name, score))
                connect.commit()
            elif user[0]['score'] < score:
                cursor.execute(f"""
                    UPDATE users
                    SET score = {score}
                    WHERE name = '{name}'
                """)
                connect.commit()

        except OperationalError as err:
            print(f'\n error: {err}')


def list_score():
    with new_connection() as connect:
        try:
            connect.row_factory = Row
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM users ORDER BY score desc")
            users = cursor.fetchall()
        except OperationalError as err:
            print(f'\n {err}')
        else:
            return users
