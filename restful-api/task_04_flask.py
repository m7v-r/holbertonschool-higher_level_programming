from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # Check if request data is valid JSON
    new_user = request.get_json()
    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is present
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user
    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == "__main__":
    app.run()
