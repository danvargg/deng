#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-09-18
Author: @danvargg
"""
import cassandra
from cassandra.cluster import Cluster

# Connect to cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Create keyspace (db)
session.execute(
    """
    CREATE KEYSPACE IF NOT EXISTS music
    WITH REPLICATION = {
        'class': 'SimpleStrategy', 
        'replication_factor': 1 
    }
    """
)

# Connect to keyspace
session.set_keyspace('music')

# Create table
query = "CREATE TABLE IF NOT EXISTS music_library"
query = query + \
    "(year INT, artist_name TEXT, album_name TEXT, PRIMARY KEY (year, artist_name))"

session.execute(query)

# Insert row
session.execute(
    """
    INSERT INTO music_library (album_name, artist_name, year)
    VALUES ('Let it be', 'Beatles', 1970)
    """)

session.execute(
    """
    INSERT INTO music_library (album_name, artist_name, year)
    VALUES ('ja ja ja', 'mmg', 2020)
    """)

rows = session.execute(
    """
    SELECT * from music_library
    """
)

for row in rows:
    print(row.year, row.album_name, row.artist_name)

rows = session.execute(
    """
    SELECT * from music_library WHERE year=1970
    """
)

for row in rows:
    print(row.year, row.album_name, row.artist_name)

# Drop table
session.execute(
    """
    DROP TABLE music_library
    """)
