class Proposal:
    def __init__(self, id, location, tasks):
        self.id = id
        self.location = location
        self.tasks = tasks

    def serialize(self):
        return {
            'id': self.id,
            'location': self.location,
            'tasks': [task.serialize() for task in self.tasks]
        }

class Task:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def serialize(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

# Mock data
proposals = [
    Proposal(0, '123 Main St, Anytown, USA', [
        Task('Task 1', 2, 50.0),
        Task('Task 2', 1, 75.0),
        Task('Task 3', 4, 25.0)
    ]),
    Proposal(1, '456 Elm St, Anytown, USA', [
        Task('Task 4', 3, 100.0),
        Task('Task 5', 2, 150.0)
    ])
]
