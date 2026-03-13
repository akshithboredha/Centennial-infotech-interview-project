from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name,email,password) VALUES (?,?,?)",
        (name,email,password)
    )

    conn.commit()
    conn.close()

    return jsonify({"message":"User registered successfully!"})

if __name__ == "__main__":
    app.run(debug=True)