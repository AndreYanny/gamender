import sqlite3
import games_table as gat

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def add_genre(name):
    genre = (name, )
    c.execute('SELECT genre_name FROM genres WHERE genre_name = ?', (name, ))
    if not c.fetchone():
        c.execute('INSERT INTO genres (genre_name) VALUES (?)', genre)
    else:
        print("Genre already exists")
    conn.commit()


def count_games(g_id):
    genre = (g_id, )
    c.execute('SELECT game_id FROM games WHERE genre_id = ?', genre)
    games_in_genre = c.fetchall()

