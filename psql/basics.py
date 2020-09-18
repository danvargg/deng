#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-09-18
Author: @danvargg
"""
import psycopg2


def connect_to_db(host, db_name, user_name, password, auto_commit=False):
    """Connects to PostgreSQL database"""
    try:
        conn = psycopg2.connect(
            f'host={host} dbname={db_name} user={user_name} password={password}')
        if auto_commit == True:
            conn.set_session(autocommit=True)  # TODO: put elsewhere
    except psycopg2.Error as e:
        print(f'\nError: Could not connect to database: \n{e}\n')
    return conn


# Connect to db
try:
    cur = connect_to_db(
        '127.0.0.1', 'music', 'daniel', 'test', auto_commit=False).cursor()
except psycopg2.Error as e:
    print(f'Error: Could not get cursor to database: \n{e}\n')

# Create table # TODO: turn into func
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS music_library (album_name VARCHAR, artist_name VARCHAR, year INT);
    """
)

# Insert rows # TODO: turn into func
cur.execute(
    """
    INSERT INTO music_library (album_name, artist_name, year)
    VALUES ('Let it be', 'Beatles', 1970)
    """
)

cur.execute(
    """
    INSERT INTO music_library (album_name, artist_name, year)
    VALUES ('ja ja ja', 'mmg', 2020)
    """
)

cur.execute(
    """
    INSERT INTO music_library (album_name, artist_name, year)
    VALUES ('poqaiweufh', 'tutu', 1920)
    """
)

# Queries
cur.execute("SELECT * FROM music_library")
cur.execute("SELECT COUNT(*) FROM music_library")
print(cur.fetchall())

# Other queries
cur.execute("SELECT * FROM music_library")
row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# Drop table
# cur.execute("DROP TABLE music_library")

if __name__ == '__main__':
    pass
