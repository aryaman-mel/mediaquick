from flask import Flask, request, jsonify, render_template_string, send_from_directory
import json, os

app = Flask(__name__, static_folder="web", static_url_path="",  template_folder="web")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/interactions", methods=["POST"])
def interactions():
    data = request.get_json()
    meds = [m.lower() for m in data.get("medicines", [])]

    # Sample hard-coded interactions
    interactions_db = {
        ("aspirin", "ibuprofen"): "May increase risk of bleeding.",
        ("warfarin", "vitamin k"): "Vitamin K may reduce warfarins effect."
    }

    found = []
    for pair, note in interactions_db.items():
        if all(p in meds for p in pair):
            found.append({"pair": pair, "note": note})

    return jsonify({"interactions": found})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
