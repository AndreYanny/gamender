import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def add_game(name, genre_id):
    game = (name, genre_id)
    c.execute('SELECT game_name FROM games_genres WHERE game_name = ?', (name, ))
    if not c.fetchone():
        c.execute('INSERT INTO games_genres (game_name, genre_id) VALUES (?, ?)', game)
    else:
        print("Game already exists")
    conn.commit()


def remove_game(g_id):
    c.execute('SELECT game_name FROM games WHERE game_name = ?', (g_id,))
    if not c.fetchone():
        print("Game does not exist")
    else:
        c.execute('DELETE FROM games WHERE game_id = ?', (g_id, ))
    conn.commit()
