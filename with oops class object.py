class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def view_tasks(self):
        print(f"{self.name} is viewing tasks")

class TeamMember(Employee):
    def submit_tasks(self):
        print(f"{self.name} is submitting tasks")

class Manager(Employee):
    def approve_tasks(self):
        print(f"{self.name} is approving tasks")

john=Manager("John","manager")
nazir=TeamMember("Nazir","team member")
john.view_tasks()
john.approve_tasks()
nazir.view_tasks()
nazir.submit_tasks()