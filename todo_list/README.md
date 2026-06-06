# Todo List Project

A console-based Todo List application built while learning Python.

This project contains two versions of the same application to demonstrate my learning progression from basic Python concepts to more structured programming techniques.

---

# Project Goals

The purpose of this project was to practice:

- Variables
- User input
- Lists
- Loops
- Conditional statements
- Functions
- Dictionaries
- Boolean values
- Program organization

---

# Project Structure

```text
todo-list/
├── basic_todo_list.py
├── advanced_todo_list.py
└── README.md
```

---

# Basic Todo List

The first version of the project.

Tasks are stored as simple strings inside a Python list.

## Features

- Add tasks
- Display tasks
- Edit tasks
- Delete tasks
- Exit the application

## Concepts Used

- Lists
- while loops
- if / elif / else
- User input
- String methods
- List methods

### Example

```text
1. Add Task
2. Display Tasks
3. Edit Task
4. Delete Task
5. Exit
```

### Limitations

- No task completion status
- No functions
- Tasks are displayed as a raw Python list
- Data is lost when the program closes

---

# Advanced Todo List

The improved version of the project.

Tasks are stored as dictionaries that contain a task name and completion status.

Example:

```python
{
    "name": "Study Python",
    "status": False
}
```

## Features

- Add tasks
- Display tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed
- Organized using functions

## Concepts Used

- Functions
- Dictionaries
- Boolean values
- enumerate()
- Data organization
- Code reusability

### Example Display

```text
1. [✘] Study Python
2. [✔] Finish assignment
3. [✘] Read book
```

### Improvements Over Basic Version

- Better code organization
- Reusable functions
- Task completion tracking
- Cleaner output
- Easier to extend

---

# How to Run

## Basic Version

```bash
python basic_todo_list.py
```

## Advanced Version

```bash
python advanced_todo_list.py
```

---

# Future Improvements

Planned features for future versions:

- Input validation
- Save tasks to a file
- Load tasks when the program starts
- Task priorities
- Due dates
- Search for tasks
- Sort tasks
- Graphical User Interface (GUI)

---

# Learning Outcome

This project helped me practice the fundamentals of Python and understand how a simple application can evolve through multiple versions.

The Basic version focuses on core programming concepts, while the Advanced version introduces better program structure and data modeling techniques.