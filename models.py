import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                visit_count INTEGER DEFAULT 0
            )
        ''')


def insert_url(original_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO urls (original_url, short_code)
            VALUES (?, ?)
        ''', (original_url, short_code))
        conn.commit()


def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
            SELECT original_url FROM urls WHERE short_code = ?
        ''', (short_code,))
        row = cur.fetchone()
        return row[0] if row else None   


def increment_visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?
        ''', (short_code,))
        conn.commit()


def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
            SELECT original_url, short_code, visit_count
            FROM urls
            ORDER BY id DESC
        ''')
        return cur.fetchall()


def delete_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            DELETE FROM urls WHERE short_code = ?
        ''', (short_code,))
        conn.commit()
