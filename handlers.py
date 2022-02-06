import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def add_handler(h_id):
    c.execute('SELECT handler_id FROM handler WHERE handler_id = ?', (h_id,))
    if not c.fetchone():
        c.execute('INSERT INTO handlers (handler_id) VALUES (?)', (h_id,))
    conn.commit()


def add_liked_games(h_id, game_id):
    c.execute('SELECT game_id FROM handlers_games WHERE handler_id = ? AND game_id = ?', (h_id, game_id))
    if not c.fetchone():
        c.execute('INSERT INTO handlers_games (handler_id, game_id) VALUES (?, ?)', (h_id, game_id))
    conn.commit()


def get_handler_liked_games(h_id):
    c.execute('SELECT game_id FROM handlers_games WHERE handler_id = ?', (h_id,))
    games = c.fetchall()
    return games


# Add User to Handlers Table
def add_user_to_handlers(u_id):
    c.execute('SELECT username FROM user WHERE user_id = ?', (u_id,))
    name = c.fetchone()
    name = name[0]
    c.execute('SELECT name FROM handler WHERE name = ?', (name,))
    if not c.fetchone():
        c.execute('INSERT INTO handler (name) VALUES (?)', (name,))
    conn.commit()
