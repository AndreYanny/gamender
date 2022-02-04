import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def add_user(name, password):
    user = (name, password)
    c.execute('SELECT username FROM users WHERE username = ?', (name, ))
    if not c.fetchone():
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', user)
    else:
        print("Username already exists")
    conn.commit()


def login(name, password):
    user = (name, password)
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', user)
    if not c.fetchone():
        print("Username and password do not match")
    else:
        print("Welcome back!")
    conn.commit()


def delete_user(u_id):
    user = (u_id, )
    c.execute('DELETE FROM users WHERE user_id = ?', user)
    conn.commit()


def change_username(u_id, name):
    user = (name, u_id)
    c.execute('SELECT username FROM users WHERE username = ?', (name,))
    if not c.fetchone():
        c.execute('UPDATE users SET username = ? WHERE user_id = ?', user)
    else:
        print("Username already exists")
    conn.commit()


def add_genres(u_id, *genres):
    c.execute('SELECT username FROM users WHERE user_id = ?', (u_id,))
    for g in genres:
        c.execute('INSERT INTO users (liked_genres) VALUES (?)', (genres,))
    conn.commit()
