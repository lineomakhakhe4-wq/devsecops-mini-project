import sqlite3
import subprocess

def dangerous(user_input):
    subprocess.call(user_input, shell=True)


def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Intentional SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)
    return cursor.fetchall()
