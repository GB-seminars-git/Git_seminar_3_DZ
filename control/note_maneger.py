import json
from datetime import datetime

from models.menu import print_message
from models.note import *
from models.text import *


class NoteControl:
    def __init__(self, file_work):
        self.file_work = file_work

    def json_note(self, note_data):
        note = Note(note_data["title"], note_data["message"])
        note.add_id(note_data["id"])
        note.created_at_date(note_data["created_date"])
        note.updated_at_date(note_data["updated_date"])
        return note

    def note_json(self, note):
        return {
            "id": note.id,
            "title": note.title,
            "message": note.message,
            "created_date": note.created_date,
            "updated_date": note.updated_date,
        }

    def load_file(self):
        try:
            with open(self.file_work, "r") as file:
                data = json.load(file)
            return [self.json_note(note_data) for note_data in data]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []

    def save_note(self, notes):
        data = [self.note_json(note) for note in notes]
        with open(self.file_work, "w") as file:
            json.dump(data, file, indent=2)

    def add_note(self, note):
        notes = self.load_file()
        if not notes:
            note.add_id(1)
        else:
            note.add_id(notes[-1].id + 1)

        time = datetime.now().isoformat()
        note.created_at_date(time)
        note.updated_at_date(time)
        notes.append(note)
        self.save_note(notes)

    def list_note(self):
        notes = self.load_file()
        if not notes:
            print_message(file_empty_msg)
        else:
            for note in notes:
                print(note)

    def edit_note_message(self, note_id: int, new_message: str):
        notes = self.load_file()
        for note in notes:
            if note.id == note_id:
                note.message = new_message
                note.updated_at_date(datetime.now().isoformat())
                break
        else:
            print_message(f"Заметка с id {note_id} не найдена.")
            return

        self.save_note(notes)
        print_message(f"Заметка с id {note_id} успешно отредактирована.")

    def filter_note_by_date(self, date):
        notes = self.load_file()
        searched_note = [note for note in notes if date in note.created_date]
        if not searched_note:
            print_message(date_filter_empty_msg + date)
        else:
            print_message(date_filter_catch_msg)
            for note in searched_note:
                print(note)

    def delete_note_by_id(self, note_id: int):
        notes = self.load_file()
        searched_note = [note for note in notes if note.id != note_id]
        if len(searched_note) == len(notes):
            print_message(f"{delete_id_not_found_msg} {note_id}")
        else:
            self.save_note(searched_note)
            print_message(f"{delete_id_successfully_msg} {note_id}")
