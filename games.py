import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


# User Adds a New Game to their Games Library
def add_game(game_name, u_id):
    c.execute('SELECT game_id FROM game WHERE game_name = ?', (game_name,))
    game_id = c.fetchone()
    c.execute('SELECT game_id FROM users_games WHERE game_id = ?', (game_id,))
    if not c.fetchone():
        c.execute('INSERT INTO users_games (user_id, game_id) VALUES (?, ?)', (u_id, game_id))
    else:
        print("Game already exists in your library")
    conn.commit()


# User Removes a Game from their Games Library
def remove_game(g_id):
    c.execute('SELECT game_name FROM game WHERE game_name = ?', (g_id,))
    if not c.fetchone():
        print("Game does not exist")
    else:
        c.execute('DELETE FROM game WHERE game_id = ?', (g_id,))
    conn.commit()


def get_game_genre(game_id):
    c.execute('SELECT genre_id FROM game WHERE game_id = ?', (game_id,))
    genre_id = c.fetchone()
    return genre_id


def get_games_by_genre(genre_id):
    c.execute('SELECT game_id FROM games_genres WHERE genre_id = ?', (genre_id,))
    games = c.fetchall()
    return games
