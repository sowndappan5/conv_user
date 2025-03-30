from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Store active users
active_users = {}

def generate_peer_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_peer_id', methods=['POST'])
def get_peer_id():
    username = request.json.get('username')
    peer_id = generate_peer_id()
    active_users[peer_id] = username
    return jsonify({"peer_id": peer_id})

@app.route('/get_active_users', methods=['GET'])
def get_active_users():
    return jsonify({"users": list(active_users.keys())})

@app.route('/remove_peer', methods=['POST'])
def remove_peer():
    peer_id = request.json.get('peer_id')
    if peer_id in active_users:
        del active_users[peer_id]
    return jsonify({"message": "Peer removed"})

if __name__ == '__main__':
    app.run(debug=True)
