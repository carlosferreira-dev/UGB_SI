import sys
sys.dont_write_bytecode = True
import sqlite3

def db_connect():
    try:
        conn = sqlite3.connect('ugb.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return None, None