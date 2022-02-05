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
    '''CREATE TABLE IF NOT EXISTS game(game_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''game_name text, '''
    '''score integer)'''
)


# Create Genres Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS genre(genre_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''genre_name text)'''
)

# Create Handler Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS handler(handler_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''name text)'''
)


# Create Tweets Table
c.execute(
    '''CREATE TABLE IF NOT EXISTS tweet(tweet_id integer PRIMARY KEY AUTOINCREMENT, '''
    '''tweet char(280), '''
    '''h_id integer, '''
    '''FOREIGN KEY (h_id) REFERENCES handler(handler_id))'''
)


# Create users_genres Table (Many-to-Many Relation)
c.execute(
    '''CREATE TABLE IF NOT EXISTS users_genres(u_id integer, '''
    '''g_id integer, '''
    '''PRIMARY KEY (u_id, g_id), '''
    '''FOREIGN KEY (u_id) REFERENCES user(user_id), '''
    '''FOREIGN KEY (g_id) REFERENCES genre(genre_id))'''
)


# Create users_handlers Table (Many-to-Many Relation)
c.execute(
    '''CREATE TABLE IF NOT EXISTS users_handlers(u_id integer, '''
    '''h_id integer, '''
    '''PRIMARY KEY (u_id, h_id), '''
    '''FOREIGN KEY (u_id) REFERENCES user(user_id), '''
    '''FOREIGN KEY (h_id) REFERENCES handler(handler_id))'''
)


# Create handlers_games Table (Many-to-Many Relation)
c.execute(
    '''CREATE TABLE IF NOT EXISTS handlers_games(h_id integer, '''
    '''g_id integer, '''
    '''PRIMARY KEY (h_id, g_id), '''
    '''FOREIGN KEY (h_id) REFERENCES handler(handler_id), '''
    '''FOREIGN KEY (g_id) REFERENCES game(game_id))'''
)


# Create games_genres Table (Many-to-Many Relation)
c.execute(
    '''CREATE TABLE IF NOT EXISTS games_genres(g_id integer, '''
    '''ge_id integer, '''
    '''PRIMARY KEY (g_id, ge_id), '''
    '''FOREIGN KEY (g_id) REFERENCES game(game_id), '''
    '''FOREIGN KEY (ge_id) REFERENCES genre(genre_id))'''
)
