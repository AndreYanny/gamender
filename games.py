import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def get_game_genre(game_id):
    c.execute('SELECT genre_id FROM game WHERE game_id = ?', (game_id,))
    genre_id = c.fetchone()
    genre_id = genre_id[0]
    return genre_id


def get_game_id(game_name):
    c.execute('SELECT game_id FROM game WHERE game_name = ?', (game_name,))
    game_id = c.fetchone()
    game_id = game_id[0]
    return game_id


def get_games_by_genre(genre_id):
    c.execute('SELECT game_id FROM games_genres WHERE genre_id = ?', (genre_id,))
    games = c.fetchall()
    return games


def add_game_score(game_name, score):
    c.execute('SELECT game_id FROM game WHERE game_name = ?', (game_name,))
    game_id = c.fetchone()
    game_id = game_id[0]
    print(game_id)
    c.execute('UPDATE game SET score = ? WHERE game_id = ?', (score, game_id))
    conn.commit()
    print(game_name + " " + str(score) + " done")
