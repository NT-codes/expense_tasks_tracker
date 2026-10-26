# Python Task and Expense Tracker

A simple command-line application built with Python and SQLite that allows users to create an account, log in, manage tasks, and record expenses. Data is stored in a local SQLite database, so it persists between program runs.

## Features

- **User Authentication:** Sign up with a username and password, or log in to an existing account.
- **Task Management:** Add multiple tasks and view saved tasks.
- **Expense Tracking:** Record expenses and view previously saved entries.
- **Persistent Storage:** Uses SQLite to store users, tasks, and expenses locally.
- **Duplicate Username Prevention:** Checks whether a username already exists before creating an account.
- **Parameterized SQL Queries:** Uses parameterized queries for database operations to help prevent SQL injection.

## Technologies Used

- **Python 3**
- **SQLite3** — Python's built-in SQLite database interface

## Project Structure

```text
task-expense-tracker/
├── expense.py          # Main application
├── tracker.db       # SQLite database (created automatically)
└── README.md        # Project documentation
```


## Prerequisites

- Python 3 installed on your system
- No external Python packages are required; `sqlite3` is included in the standard library.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd task-expense-tracker
```

### 2. Run the application

```bash
python expense.py
```

On Windows, you can also use:

```powershell
py expense.py
```

The application creates `tracker.db` and its required tables automatically when run for the first time.

## How to Use

### 1. Sign up or log in

Choose one of the options displayed at startup:

- `1` — Log in with an existing account.
- `2` — Create a new account.

After successful registration, you can log in using your new credentials.

### 2. Main menu

Once logged in, choose an action:

| Option | Action |
|---|---|
| 1 | View tasks |
| 2 | Add tasks |
| 3 | View expenses |
| 4 | Add an expense |
| 5 | Exit |

### 3. Add tasks or expenses

Enter each task or expense when prompted. Type `exit` to stop entering items.

Your entries are saved to the SQLite database.

## Database Schema

The application uses three tables:

| Table | Columns | Purpose |
|---|---|---|
| `users` | `username`, `password` | Stores account credentials |
| `tasks` | `task` | Stores task descriptions |
| `expenses` | `expense` | Stores expense entries |

## Current Limitations

- Passwords are stored as plain text. A real application should use a suitable password-hashing algorithm.
- Tasks and expenses are not associated with individual users, so entries are shared across accounts.
- Expenses are stored as text rather than structured amounts and categories.
- The application does not currently support editing or deleting tasks and expenses.
- Some invalid inputs, such as non-numeric menu selections, may cause errors.

## Future Improvements

- Associate tasks and expenses with the logged-in user.
- Hash passwords securely.
- Store expense amounts, dates, and categories separately.
- Add options to edit, delete, and mark tasks as completed.
- Add input validation and error handling.
- Generate expense summaries and monthly reports.
- Build a graphical interface or web application.

## Learning Objectives

This project demonstrates practical use of:

- Python functions and control flow
- Loops and conditional statements
- User input and command-line interaction
- SQL queries and database operations
- SQLite integration with Python
- Basic account registration and login logic

## License

This project is available for educational and personal learning purposes. Add a specific open-source license if you intend to distribute it.
