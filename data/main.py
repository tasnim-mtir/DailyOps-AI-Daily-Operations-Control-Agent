from flask import Flask, jsonify
import json

app = Flask(__name__)

# ---------- LOAD JSON FILES ----------

# Change filenames here if your files have different names
with open("emails.json", "r", encoding="utf-8") as f:
    emails_data = json.load(f)

with open("tasks.json", "r", encoding="utf-8") as f:
    tasks_data = json.load(f)

with open("meetings.json", "r", encoding="utf-8") as f:
    meetings_data = json.load(f)

# ---------- ROUTES (ENDPOINTS) ----------

@app.route("/")
def root():
    return jsonify({
        "message": "OpsFlow JSON API is running. Available endpoints: /emails, /tasks, /meetings"
    })

@app.route("/emails", methods=["GET"])
def get_emails():
    return jsonify(emails_data)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks_data)

@app.route("/meetings", methods=["GET"])
def get_meetings():
    return jsonify(meetings_data)


# ---------- REPLIT ENTRY POINT ----------

if __name__ == "__main__":
    # Replit normally uses host='0.0.0.0' and port 8000
    app.run(host="0.0.0.0", port=8000)
