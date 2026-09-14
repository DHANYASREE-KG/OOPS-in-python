
#defining the fucntion

def login(user_data):
    print(f"Logging in as {user_data['name']}")

def view_tasks(user_data):
    print(f"{user_data['name']} is viewing tasks")

def submit_tasks(user_data):
    if user_data['role'] != 'team member':
        print(f"{user_data['name']} is not authorized to submit tasks")
    print(f"{user_data['name']} is submitting tasks")

def assign_tasks(user_data):
    if user_data['role'] != 'manager':
        print(f"{user_data['name']} is not authorized to assign tasks")
    print(f"{user_data['name']} is assigning tasks")
#data collection
user_data={
    "name":'john',
    "role":"manager"
}
login(user_data)
view_tasks(user_data)
submit_tasks(user_data)
assign_tasks(user_data)