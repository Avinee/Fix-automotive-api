from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

users = {"test@example.com": "password123"}
appointments = []

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    if users.get(email) == password:
        return jsonify({"token": "dummy-token-for-now"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/appointments", methods=["POST"])
def book_appointment():
    data = request.json
    appointments.append(data)
    return jsonify({"message": "Appointment booked", "data": data})

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({"message": "File uploaded", "filename": filename})

@app.route("/")
def home():
    return "Fix Automotive API is running!"

if __name__ == "__main__":
    app.run(debug=True)
