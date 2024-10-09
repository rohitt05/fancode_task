import requests

def get_users():
    url = "http://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def filter_fancode_users(users):
    """Filtering the users by city FanCode (latitude between -40 to 5 and long between 5 to 100)"""
    fancode_users = [
        user for user in users
        if -40 <= float(user['address']['geo']['lat']) <= 5 and 5 <= float(user['address']['geo']['lng']) <= 100
    ]
    return fancode_users

def get_user_todos(user_id):
    url = f"http://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    return response.json()

def calculate_completion_percentage(todos):
    """ Here we are calculating the percentage of completed tasks"""
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    if total_tasks == 0:
        return 0  
    return (len(completed_tasks) / total_tasks) * 100

def verify_fancode_users_completion():
    users = get_users()
    fancode_users = filter_fancode_users(users)
    
    for user in fancode_users:
        todos = get_user_todos(user['id'])
        completion_percentage = calculate_completion_percentage(todos)
        if completion_percentage <= 50:
            print(f"User {user['name']} has only completed {completion_percentage}% of tasks.")
        else:
            print(f"User {user['name']} meets the requirement with {completion_percentage}% completed tasks.")

if __name__ == "__main__":
    verify_fancode_users_completion()
