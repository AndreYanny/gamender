import sqlite3

# Create Database
conn = sqlite3.connect('gamender.db')
c = conn.cursor()

# Create Users Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS users(user_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''username text, '''
    '''password text, '''
    '''liked_genres text [])'''
)

# Create Games Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS games(game_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''game_name text, '''
    '''genre text, '''
    '''score integer)'''
)

# Create Handler Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS handler(handler_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''name text, '''
    '''liked_games text [], '''
    '''similar_handlers text [])'''
)


# Create Tweets Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS tweet(tweet_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''tweet char(280), '''
    '''FOREIGN KEY (handler_id) REFERENCES genres(handler_id))'''
)
