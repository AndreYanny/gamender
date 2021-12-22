import sqlite3

# Create Database
conn = sqlite3.connect('gamender.db')
c = conn.cursor()

# Create Users Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS users(user_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''username text, '''
    '''password text)'''
)

# Create Games Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS games(game_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''game_name text, '''
    '''FOREIGN KEY (genre_id) REFERENCES genres(genre_id))'''
)

# Create Genres Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS genres(genre_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''genre_name text)'''
)

# Create Handlers Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS handlers(handler_id integer PRIMARY KEY)'''
)
