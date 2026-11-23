# Task API

A REST API that lets you create, view, update, and delete tasks. I built it with Python, Flask, and SQLite to understand how to handle tasks and work with a database while learning the Flask framework.

## Features

- Create a task
- Retrieve all tasks
- Update a task's title or done status
- Delete a task

## Built with

- Python, Flask, SQLite

## How to run it

1. Clone the repository and go into the folder
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Start the server:
   ```
   python app.py
   ```
5. The API runs at `http://127.0.0.1:5000`

## Endpoints

| Method | Address | What it does |
|--------|---------|--------------|
| GET | `/tasks` | Returns a list of all tasks |
| POST | `/tasks` | Adds a new task |
| PUT | `/tasks/{id}` | Changes or updates a specified task |
| DELETE | `/tasks/{id}` | Removes a specified task |

## Example

A task must be created first, and then it can be updated.

Add a task:

```bash
curl -i -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Learn Flask"}'
```

Response:

```
HTTP/1.1 201 CREATED

{
  "done": false,
  "id": 1,
  "title": "Learn Flask"
}
```

Update it:

```bash
curl -i -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "New title"}'
```

Response:

```
HTTP/1.1 200 OK

{
  "done": false,
  "id": 1,
  "title": "New title"
}
```

## What I learned
I really enjoyed taking on this project because it made me understand some concepts. I understood CRUD tasks and alo error codes. I learnt how to explain my line of code and understand what those lines mtranslates to. 