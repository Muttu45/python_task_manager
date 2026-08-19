class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data["priority"]
        )

    def display(self, index):
        print(f"{index}. {self.name}")
        print(f"   Description: {self.description}")
        print(f"   Priority: {self.priority}")
