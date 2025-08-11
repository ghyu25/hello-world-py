from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Serve index.html
@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

# API endpoint
@app.route("/api/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
