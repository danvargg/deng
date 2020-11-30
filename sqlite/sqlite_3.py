#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-11-25
Author: @danvargg
"""
import sqlite3

db = sqlite3.connect('contacts.sqlite')

db.execute(
    """
    CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)
    """
)

db.execute(
    """
    INSERT INTO contacts (name, phone, email) VALUES ('kkk', 6524881, 'tim@gmail.com')
    """
)

update_query = "UPDATE contacts SET email = 'updated@gmail.com' WHERE contacts.name = 'kkk'"
update_cursor = db.cursor()
update_cursor.execute(update_query)
update_cursor.close()

cursor = db.cursor()
cursor.execute(
    """
    SELECT * FROM contacts
    """
)
for name, phone, email in cursor:
    print(name, phone, email)
# cursor.close()
# db.commit()
db.close()
