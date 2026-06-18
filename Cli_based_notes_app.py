
import json

try:
    with open("notes.json","r") as file:
        notes = json.load(file)
except:
    notes = {}

def print_note_keys():
    for i in notes.keys():
        print(i)

def add_note():
    title = input("Enter note title: ")
    note = input("Enter note: ")

    '''temp_list = {title : note}
    notes.update(temp_list)'''

    notes[title] = note

def view_note():
    if notes == {}:
        print("No notes found\n")
    else:
        print_note_keys()
        cnf = input("Do you want to open a note? (y/n):")
        if cnf == "y":
            view_title = input("Enter title: ")
            print(notes.get(view_title))
        else:
            pass

def delete_note():
    print_note_keys()
    pop_title = input("Enter title of note to delete it: ")
    cnf = input("Are you sure? (y/n): ")
    if cnf == "y":
        notes.pop(pop_title)
        print(f"Note with title {pop_title} deleted")
    else:
        print("Note not deleted.")

def edit_note():
    print_note_keys()
    edit_title = input("Enter title of note to edit it: ")
    cnf = input("Are you sure? (y/n): ")
    if cnf == "y":
        new_note = input("Enter new note: ")
        notes[edit_title] = new_note
    else:
        print("Note not edit.")

def json_save():
    with open("notes.json","w") as file:
        json.dump(notes,file)

while True:
    print("\n1. Add note\n")
    print("2. View note\n")
    print("3. Delete note\n")
    print("4. Edit note\n")
    print("5. Exit")
    num = input("Enter option num:")

    if num == "1":
        add_note()
        json_save()

    elif num == "2":
        view_note()

    elif num == "3":
        delete_note()
        json_save()

    elif num == "4":
        edit_note()
        json_save()

    elif num == "5":
        break
    else:
        print("Enter valid number.")

