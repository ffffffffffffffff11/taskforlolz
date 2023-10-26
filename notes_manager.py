# notes_manager.py
from db import NotesDatabase

class NotesManager:
    def __init__(self, db_name):
        self.db = NotesDatabase(db_name)

    def add_note(self, title, content):
        self.db.add_note(title, content)

    def view_all_notes(self):
        return self.db.get_all_notes()

    def get_note_by_id(self, note_id):
        all_notes = self.view_all_notes()
        for note in all_notes:
            if str(note[0]) == note_id:
                return note
        return None

    def search_notes(self, keyword):
        return self.db.search_notes(keyword)

    def delete_note(self, note_id):
        self.db.delete_note(note_id)

    def close(self):
        self.db.close()
