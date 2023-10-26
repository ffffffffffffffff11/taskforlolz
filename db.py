# db.py
import sqlite3

class NotesDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # Создание таблицы для хранения заметок
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()

    def add_note(self, title, content):
        # Добавление новой заметки
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        self.conn.commit()

    def get_all_notes(self):
        # Получение списка всех заметок
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM notes')
        return cursor.fetchall()

    def search_notes(self, keyword):
        # Поиск заметок по ключевому слову
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()

    def delete_note(self, note_id):
        # Удаление заметки по ID
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
