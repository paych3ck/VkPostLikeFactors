import sqlite3
import csv

connection = sqlite3.connect('Sobyanin_posts_data.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        post_id INTEGER PRIMARY KEY,
        time_of_day TEXT,
        day_of_week TEXT,
        full_date TEXT,
        likes_count INTEGER
    )
''')

with open('Sobyanin_posts_data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    connection.executemany('INSERT INTO posts VALUES (?, ?, ?, ?, ?)', csv_reader)

connection.commit()
connection.close()