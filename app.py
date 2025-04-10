from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from melda ECS Container"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use 8080 from Cloud Run
    app.run(host="0.0.0.0", port=port)
