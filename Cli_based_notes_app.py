
import json

try:
    with open("notes.json","r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = {}

def print_note_keys():
    print("\n===========")
    print("   Notes   ")
    print("===========\n")
    count=1
    for i in notes.keys():
        print(f"{count}.{i}")
        count+=1
    count=1
    print("\n===========\n")

def validate_title(title):
    if title in notes:
        return True

    print("\n->Enter valid title from list.")
    return False

def add_note():
    while True:
        title = input("\nEnter note title: ")

        if not title:
            print("\n->The title of the note cannot be empty.")
            continue
        elif title in notes:
            print("\nThe mentioned title already exists in the library")
            cnf=input("Do you want to overwrite it(y/n):")
            if cnf=="n":
                continue
            elif cnf=="y":
                print(f"\nThis will overwrite the following data: {notes.get(title)}")
                cnf=input("Do you confirm(y/n): ")
                if cnf=="y":
                    break
                continue
                    
        break

    note = input("Enter note: ")

    '''temp_list = {title : note}
    notes.update(temp_list)'''

    notes[title] = note

def view_note():
    if not notes:
        print("No notes found\n")
    else:
        print_note_keys()
        
        cnf = input("Do you want to open a note? (y/n):")
        if cnf == "y":
            
            while True:

                view_title = input("\nEnter title: ")
                
                if not validate_title(view_title):
                    continue
                break
            if not notes.get(view_title):
                print("\n--------------------")
                print("The note is empty")
                print("--------------------")
            else:
                print("\n--------------------")
                print(f"-> {notes.get(view_title)}")
                print("--------------------")

def search_note(title):
    match=  [k for k in notes if title.lower() in k.lower()]

    if match:
        print("--------------")
        print("    RESULTS   ")
        print("--------------")
        count = 1
        for i in match:
            print(f"{count}. {i}")
            count+=1
        count = 1

        cnf=input("\nDo you want to view a note(y/n):")
        if cnf=="y":
            while True:
                title = input("\nEnter note title to view: ")
                if not validate_title(title):
                    continue
                break
            print("\n--------------")
            print(f"-> {notes.get(title)}")
            print("--------------\n")
    else:
        print("\nNote not found")
        


def delete_note():
    
    print_note_keys()
    
    while True:
        pop_title = input("\nEnter title of note to delete it: ")
        if not validate_title(pop_title):
            continue
        break

    cnf = input("\nAre you sure? (y/n): ")
    if cnf == "y":
        notes.pop(pop_title)
        print(f"\nNote with title {pop_title} is deleted")
    else:
        print("\nNote not deleted.")

def edit_note():
    print_note_keys()
    choice = input("Do you want to rename title? Or edit a note (title/note):")
    if choice == "note":
        while True:
            edit_title = input("Enter title of note to edit it's content: ")
            if not validate_title(edit_title):
                continue
            break
        cnf = input("Are you sure? (y/n): ")
        if cnf == "y":
            new_note = input("Enter new note: ")
            notes[edit_title] = new_note
        else:
            print("Note not edit.")
    elif choice == "title":
        while True:
            edit_title = input("Enter title you want to rename: ")
            if not validate_title(edit_title):
                continue
            data = notes.get(edit_title)
            break
        while True: 
            new_title = input("Enter new title: ")
            if new_title in notes:
                print(f"A note with title {new_title} already exists.")
                continue
            break
        notes[new_title] = data
        notes.pop(edit_title)

def json_save():
    with open("notes.json","w") as file:
        json.dump(notes,file,indent = 4)

while True:
    print("\n1. Add note\n")
    print("2. View note\n")
    print("3. Search note\n")
    print("4. Delete note\n")
    print("5. Edit note\n")
    print("6. Exit")
    num = input("\nEnter option num:")

    if num == "1":
        add_note()
        json_save()

    elif num == "2":
        view_note()

    elif num == "3":
        print_note_keys()
        title = input("Enter title of note to search:")
        search_note(title)

    elif num == "4":
        delete_note()
        json_save()

    elif num == "5":
        edit_note()
        json_save()

    elif num == "6":
        break
    else:
        print("Enter valid number.")

