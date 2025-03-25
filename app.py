from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_bot():
    subprocess.Popen(["python", "bot.py"])

@app.route('/start-bot')
def start_bot():
    run_bot()
    return jsonify({"message": "Bot started successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
