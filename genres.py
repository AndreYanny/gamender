import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()


def get_genre_name(ge_id):
    c.execute('SELECT genre_name FROM genre WHERE genre_id = ?', (ge_id,))
    genre_name = c.fetchone()
    genre_name = genre_name[0]
    return genre_name


def get_genre_id(ge_name):
    c.execute('SELECT genre_id FROM genre WHERE genre_name = ?', (ge_name,))
    genre_id = c.fetchone()
    genre_id = str(genre_id[0])
    return genre_id


# Get Top Game in a Genre
def get_top_game(genre_id):
    c.execute('SELECT game_id, MAX(score) FROM game WHERE genre_id = ?', (genre_id,))
    top_game = c.fetchone()
    top_game = top_game[0]
    return top_game
