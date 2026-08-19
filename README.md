# Python Task Manager Application

A console-based Task Manager Application built with Python.

## Features

- Add tasks
- View all tasks
- Update existing tasks
- Delete tasks with confirmation
- Priority validation
- JSON persistent storage
- Input validation
- Regular expression validation
- Error handling
- Object-Oriented Programming
- Modular project structure

## Task Information

Each task contains:

- Name
- Description
- Priority

Allowed priorities:

- High
- Medium
- Low

## Project Structure

```text
python_task_manager/
│
├── data/
│   └── tasks.json
│
├── task_manager_app/
│   ├── __init__.py
│   ├── task.py
│   ├── file_handler.py
│   └── input_validator.py
│
├── main.py
└── README.md
