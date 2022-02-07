import sqlite3
import os
import games as g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()


def get_user_name(u_id):
    c.execute('SELECT username FROM user WHERE user_id = ?', (u_id,))
    u_name = c.fetchone()
    u_name = u_name[0]
    return u_name


def get_user_id(u_name):
    c.execute('SELECT user_id FROM user WHERE username = ?', (u_name,))
    u_id = c.fetchone()
    u_id = u_id[0]
    return u_id


# User Makes an Account (Register)
def add_user(name, password):
    user = (name, password)
    c.execute('SELECT username FROM user WHERE username = ?', (name,))
    if not c.fetchone():
        c.execute('INSERT INTO user (username, password) VALUES (?, ?)', user)
    else:
        print("Username already exists")
    conn.commit()


def login(name, password):
    user = (name, password)
    c.execute('SELECT * FROM user WHERE username = ? AND password = ?', user)
    if not c.fetchone():
        print("Username and password do not match")
    else:
        print("Welcome back!")
    conn.commit()


def delete_user(u_id):
    c.execute('DELETE FROM users WHERE user_id = ?', (u_id,))
    conn.commit()


def change_username(u_id, name):
    user = (name, u_id)
    c.execute('SELECT username FROM users WHERE username = ?', (name,))
    if not c.fetchone():
        c.execute('UPDATE users SET username = ? WHERE user_id = ?', user)
    else:
        print("Username already exists")
    conn.commit()


# User Adds a New Game to their Games Library
def add_game(game_name, u_id, game_review):
    c.execute('SELECT game_id FROM game WHERE game_name = ?', (game_name,))
    game_id = c.fetchone()
    game_id = game_id[0]
    c.execute('SELECT game_id FROM users_games WHERE game_id = ?', (game_id,))
    if not c.fetchone():
        c.execute('INSERT INTO users_games (user_id, game_id, review) VALUES (?, ?, ?)', (u_id, game_id, game_review))
    else:
        print("Game already exists in your library")
    conn.commit()


# User Removes a Game from their Games Library
def remove_game(game_name, u_id):
    c.execute('SELECT game_id FROM game WHERE game_name = ?', (game_name,))
    game_id = c.fetchone()
    game_id = game_id[0]
    c.execute('SELECT game_id FROM users_games WHERE user_id = ? AND game_id = ?', (u_id, game_id))
    if not c.fetchone():
        print("Game does not exist")
    else:
        c.execute('DELETE FROM users_games WHERE user_id = ? AND game_id = ?', (u_id, game_id))
    conn.commit()


# User Adds their Favourite Genres
def add_genre(genre_name, u_id):
    c.execute('SELECT genre_id FROM genre WHERE genre_name = ?', (genre_name,))
    genre_id = c.fetchone()
    genre_id = genre_id[0]
    c.execute('SELECT * FROM users_genres WHERE user_id = ? AND genre_id = ?', (u_id, genre_id))
    if not c.fetchone():
        c.execute('INSERT INTO users_genres (user_id, genre_id) VALUES (?, ?)', (u_id, genre_id))
    conn.commit()


# Return User's Favourite Genres
def get_fav_genres(u_id):
    c.execute('SELECT genre_id FROM users_genres WHERE user_id = ?', (u_id,))
    genres = c.fetchall()
    return genres


# Remove a Genre from the User's Favourite Genres
def delete_genre(genre_name, u_id):
    c.execute('SELECT genre_id FROM genre WHERE genre_name = ?', (genre_name,))
    genre_id = c.fetchone()
    genre_id = genre_id[0]
    c.execute('DELETE FROM users_genres WHERE user_id = ? AND genre_id = ?', (u_id, genre_id))
    conn.commit()


# Get User Game Review (0 or 1)
def get_game_review(u_id, game_name):
    game_id = g.get_game_id(game_name)
    c.execute('SELECT review FROM users_games WHERE user_id = ? AND game_id = ?', (u_id, game_id))
    game_review = c.fetchone()
    game_review = game_review[0]
    return game_review


# Return All the Games Liked by a User
def get_user_games(u_id):
    c.execute('SELECT game_id FROM users_games WHERE user_id = ?', (u_id,))
    games = c.fetchall()
    listed_games = []
    for i in games:
        listed_games.append(i[0])
    return listed_games
