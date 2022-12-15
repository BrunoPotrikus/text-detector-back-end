import sqlite3
import os

def connectBD(email, password):

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    print(f'Email: {email}')
    print(f'Senha: {password}')

    cur.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)')

    if os.path.isfile('/tmp/insertok'):
        print("", end="")
    else:
        cur.execute(f'INSERT INTO users (email, password) VALUES ({email}, {password})')
        f = open("/tmp/insertok", "a")
        f.write("insertok")
        f.close()

    conn.commit()
    conn.close()
