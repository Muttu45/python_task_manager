import json
from pathlib import Path

from .task import Task


DATA_FILE = Path("data/tasks.json")


def load_tasks():
    try:
        if not DATA_FILE.exists():
            return []

        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid task data. Starting with an empty task list.")
            return []

        return [Task.from_dict(item) for item in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON.")
        return []

    except (KeyError, TypeError, OSError) as error:
        print(f"Error loading tasks: {error}")
        return []


def save_tasks(tasks):
    try:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        data = [task.to_dict() for task in tasks]

        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except (OSError, TypeError) as error:
        print(f"Error saving tasks: {error}")
