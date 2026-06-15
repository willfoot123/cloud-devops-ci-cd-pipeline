from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "DevOps CI/CD Pipeline API",
        "status": "Running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": "Production (AWS EC2)",
        "message": "Application successfully deployed via CI/CD pipeline"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "Healthy",
        "uptime_check": "OK"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
