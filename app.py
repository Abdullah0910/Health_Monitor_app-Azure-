from flask import Flask, jsonify, render_template
from prometheus_client import Counter, generate_latest
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    services = {
        "POS_API": "Healthy" if random.random() > 0.2 else "Degraded",
        "PaymentGateway": "Healthy" if random.random() > 0.1 else "Down",
        "InventoryService": "Healthy"
    }
    return render_template("index.html", services=services)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4'}

@app.route('/health')
def health():
    return jsonify(status="ok", uptime=f"{time.time()}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
@app.route("/health")
def health():
    return "OK", 200
