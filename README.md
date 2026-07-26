# CLI Notes App

A simple command-line notes application built in Python.

> This project was created as a learning project to practice Python fundamentals, file handling, JSON persistence, and CRUD operations.

This project allows users to create, view, search, edit, rename, and delete notes. Notes are stored in a JSON file so they remain available even after the program is closed.

---

## Features

* Add new notes
* View saved notes
* Search notes by title
* Edit note contents
* Rename note titles
* Delete notes
* JSON-based persistent storage
* Input validation for common user errors

---

## Technologies Used

* Python
* JSON 

---

## Project Structure

```
main.py        # Main application
notes.json     # Stores all notes
```

---

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

The application will automatically create `notes.json` if it does not already exist.

---

## What I Learned

This project helped me understand:

* Python functions
* Dictionaries
* File handling
* JSON serialization and deserialization
* CRUD (Create, Read, Update, Delete) operations
* Input validation
* Refactoring repeated code into reusable functions
* Designing a simple command-line application

---

## Future Improvements

Some features I would like to add in future versions:

* Note categories or tags
* Sorting notes
* Date and time for each note
* Database support
* Graphical user interface (GUI)

---

## Version

Current Release: **v1.0**

## Development Journey

- Started by storing notes in Python lists.
- Switched to dictionaries to organize notes using titles as keys.
- Introduced JSON storage to make notes persistent between program runs.
- Added searching, editing, renaming, and input validation.
- Refactored repeated code into reusable helper functions.
- Improved the user interface with clearer menus and better formatted output.