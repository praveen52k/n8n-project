from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

SERVER_NAME = os.environ.get("SERVER_NAME", "my-app")
PORT = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return jsonify({"server": SERVER_NAME, "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    print(f"Starting {SERVER_NAME} on port {PORT}...")
    app.run(host='0.0.0.0', port=PORT)
