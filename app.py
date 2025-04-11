from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from nambath ECS Container"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/<path:path>")
def catch_all(path):
    return f"❌ No route found for /{path}", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
