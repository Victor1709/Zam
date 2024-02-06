import json

class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteManager:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(note_data['id'], note_data['title'], note_data['body'], note_data['timestamp'])
                    self.notes.append(note)
        except FileNotFoundError:
            print("No existing notes found.")

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append({'id': note.id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp})

        with open('notes.json', 'w') as file:
            json.dump(data, file)

    def print_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}\nTitle: {note.title}\nBody: {note.body}\nTimestamp: {note.timestamp}\n")

    def add_note(self, id, title, body, timestamp):
        note = Note(id, title, body, timestamp)
        self.notes.append(note)
        print("Note added successfully.")

    def edit_note(self, id, new_title, new_body):
        for note in self.notes:
            if note.id == id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.datetime.now()
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                print("Note deleted successfully.")
                return
        print("Note not found.")

if __name__ == '__main__':
    note_manager = NoteManager()
    note_manager.load_notes()

    while True:
        print("1. List notes\n2. Add note\n3. Edit note\n4. Delete note\n5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            note_manager.print_notes()
        elif choice == '2':
            id = input("Enter note ID: ")
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            timestamp = datetime.datetime.now()
            note_manager.add_note(id, title, body, timestamp)
        elif choice == '3':
            id = input("Enter note ID to edit: ")
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            note_manager.edit_note(id, new_title, new_body)
        elif choice == '4':
            id = input("Enter note ID to delete: ")
            note_manager.delete_note(id)
        elif choice == '5':
            note_manager.save_notes()
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")