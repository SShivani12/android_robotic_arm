from flask import Flask, request, jsonify
from main import RoboticArm

app = Flask(__name__)
arm = RoboticArm()

@app.route('/move', methods=['POST'])
def move_arm():
     data = request.json
     command = data.get("command", "")
     arm.move(command)
     return jsonify({"status": "moved", "command": command, "state": arm.status()})
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
