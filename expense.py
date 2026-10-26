import sqlite3

# ----------------- Database Setup -----------------
conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

# Create tables if they do not exist yet
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)"""
)
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (task TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (expense TEXT)""")
conn.commit()
# --------------------------------------------------


def get_all_tasks():
    cursor.execute("SELECT task FROM tasks")
    return [row[0] for row in cursor.fetchall()]


def get_all_expenses():
    cursor.execute("SELECT expense FROM expenses")
    return [row[0] for row in cursor.fetchall()]


def view_tasks():
    tasks_list = get_all_tasks()
    if len(tasks_list) == 0:
        print("No tasks, please add more tasks")
        print("1. Add task")
        print("2. Exit")
        x = input("Please pick 1 or 2: ")
        if x == "1":
            tasks(2)
    else:
        for i in range(len(tasks_list)):
            print(f"{i+1}. {tasks_list[i]}")


def add_tasks():
    print("Note : Please type exit when you are done adding the tasks")
    print("Please enter the tasks: ")
    i = 1
    while True:
        a = input(f"{i}. ")
        if a.lower() == "exit":
            break
        # Save directly to database
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (a,))
        conn.commit()
        i += 1


def view_expense():
    expense_list = get_all_expenses()
    if len(expense_list) == 0:
        print("No expenses yet")
        print("1. Add New expense")
        print("2. Exit")
        x = input("Please pick 1 or 2: ")
        if x == "1":
            add_expense()
    else:
        for i in range(len(expense_list)):
            print(f"{i+1}. {expense_list[i]}")


def add_expense():
    print("Note : Please type exit when you are done adding the expenses")
    print("Please enter the expenses: ")
    i = 1
    while True:
        a = input(f"{i}. ")
        if a.lower() == "exit":
            break
        # Save directly to database
        cursor.execute("INSERT INTO expenses (expense) VALUES (?)", (a,))
        conn.commit()
        i += 1


def tasks(input_user):
    if input_user == 1:
        return view_tasks()
    elif input_user == 2:
        return add_tasks()
    elif input_user == 3:
        return view_expense()
    elif input_user == 4:
        return add_expense()


def main_menu():
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. View expenses")
    print("4. Add an expense")
    print("5. Exit")

    input_1 = int(input("Select an option: "))
    attempts = 1
    while True:
        if input_1 > 5 or input_1 < 1:
            print("please enter a number through 1 to 5, thank you")
            input_1 = int(input("Select an option: "))
            attempts += 1
            if attempts == 5:
                input_1 = 5
                break
        else:
            if input_1 != 5:
                tasks(input_1)
            break


print(
    "---------------**__Welcome to task and expense tracker__**---------------"
)
print("1. login")
print("2. signup")

l_s = int(input("Pick 1 or 2: "))

if l_s == 2:
    taken = False
    while taken == False:
        user_name = input("please enter a username: ")

        # Check if username exists in database
        cursor.execute(
            "SELECT username FROM users WHERE username = ?", (user_name,)
        )
        if cursor.fetchone():
            print("Username already taken")
        else:
            pass_word = input("Please enter a password: ")
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (user_name, pass_word),
            )
            conn.commit()
            print("Thank you for making an account now you may login")
            l_s = 1
            taken = True

if l_s == 1:
    user_name = input("Please enter your username: ")

    # Fetch stored password from database
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (user_name,)
    )
    user_row = cursor.fetchone()

    if not user_row:
        print("username not found!!")
    else:
        correct_password = False
        while correct_password == False:
            pass_word = input("Please enter the password: ")
            if user_row[0] == pass_word:
                correct_password = True
                main_menu()
            else:
                print("wrong password please try again")

