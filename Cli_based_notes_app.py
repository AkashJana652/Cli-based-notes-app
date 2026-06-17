
notes = {}

while True:
    print("1. Add note\n")
    print("2. View note\n")
    print("3. Delete note\n")
    print("4. Edit note\n")
    print("5. Exit")
    num = input("Enter option num:")

    if num == "1":
        title=input("Enter note title: ")
        
        '''temp_list = {title : note}
        notes.update(temp_list)'''

        notes[title]=input("Enter note: ")

    elif num == "2":
        print(notes.keys())
        view_title = input("Enter title: ")
        print(notes.get(view_title))

    elif num == "3":
        print(notes.keys())
        pop_title = input("Enter title of note to delete it: ")
        cnf = input("Are you sure? (y/n): ")
        if cnf == "y":
            notes.pop(pop_title)
        else:
            print("Note not deleted.")
    elif num == "4":
        pass
    elif num == "5":
        break
    else:
        print("Enter valid number.")

