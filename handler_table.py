import sqlite3

conn = sqlite3.connect('gamender.db')
c = conn.cursor()


def add_handler(h_id):
    c.execute('SELECT username FROM handler WHERE handler_id = ?', (h_id, ))
    if not c.fetchone():
        c.execute('INSERT INTO handlers (handler_id) VALUES (?)', (h_id, ))
    conn.commit()
