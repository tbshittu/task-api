from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = "tasks.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS tasks ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "title TEXT NOT NULL, "
        "done INTEGER NOT NULL DEFAULT 0)"
    )
    conn. commit()
    conn.close()

init_db()



@app.route("/")
def home():
    return "Task API is running"


@app.route("/tasks")
def get_tasks():
    conn = get_db()
    rows = conn.execute("SELECT * FROM tasks"). fetchall()
    conn.close()
    result = [
        {"id": row["id"],"title": row["title"], "done": bool(row["done"])}
        for row in rows
    ]
    return jsonify(result)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True)
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    conn = get_db()
    cursor = conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_id, "title": data["title"], "done": False}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"})

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Data is required"}), 400
    conn = get_db()
    row = conn.execute("SELECT * FROM tasks WHERE id = ? ", (task_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Task not found"}), 404
    title = data.get("title", row["title"])
    done = data.get("done", bool(row["done"]))
    conn.execute("UPDATE tasks SET title = ? , done = ? WHERE id = ?", (title, int(done), task_id))
    conn.commit()
    conn.close()
    return jsonify({"id": task_id, "title": title, "done": bool(done)})

if __name__ == "__main__":
    app.run(debug=True)