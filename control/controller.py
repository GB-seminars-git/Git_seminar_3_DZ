from control.note_maneger import *
from models.menu import *


def start():
    file = "C:/learning/Notes_app_Python_for_GB/data_storage/notebook_hab.json"
    manager = NoteControl(file)

    while True:
        choice = main_menu()

        match choice:
            case 1:
                title = input(title_request_msg)
                message = input(message_request_msg)
                note = Note(title, message)
                manager.add_note(note)
                print_message(note_add_complete_msg)
            case 2:
                manager.list_note()
            case 3:
                note_id = int(input(id_request_for_correcting_msg))
                new_message = input(enter_new_message_msg)
                manager.edit_note_message(note_id, new_message)
            case 4:
                date = input(date_request_msg)
                manager.filter_note_by_date(date)
            case 5:
                note_id = int(input(id_request_for_delete_msg))
                manager.delete_note_by_id(note_id)
            case 6:
                break

