
notes = {}

def add_note():
    title = input("Enter note title: ")
    note = input("Enter note: ")

    '''temp_list = {title : note}
    notes.update(temp_list)'''

    notes[title] = note

def view_note():
    print(notes.keys())
    cnf = input("Do you want to open a note? (y/n):")
    if cnf == "y":
        view_title = input("Enter title: ")
        print(notes.get(view_title))
    else:
        pass

def delete_note():
    print(notes.keys())
    pop_title = input("Enter title of note to delete it: ")
    cnf = input("Are you sure? (y/n): ")
    if cnf == "y":
        notes.pop(pop_title)
    else:
        print("Note not deleted.")

while True:
    print("1. \nAdd note\n")
    print("2. View note\n")
    print("3. Delete note\n")
    print("4. Edit note\n")
    print("5. Exit")
    num = input("Enter option num:")

    if num == "1":
        add_note()

    elif num == "2":
        view_note()

    elif num == "3":
        delete_note()
    elif num == "4":
        pass
    elif num == "5":
        break
    else:
        print("Enter valid number.")

