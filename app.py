from flask import Flask, request, jsonify, render_template
from image_ai.enhance import enhance_image
from image_ai.remove_bg import remove_background
from image_ai.color_fix import fix_colors
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/edit", methods=["POST"])
def edit_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    action = request.form.get("action")

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, file.filename)

    file.save(input_path)

    if action == "enhance":
        enhance_image(input_path, output_path)
    elif action == "remove_bg":
        remove_background(input_path, output_path)
    elif action == "color_fix":
        fix_colors(input_path, output_path)
    else:
        return jsonify({"error": "Invalid action"}), 400

    return jsonify({
        "status": "success",
        "output_image": output_path
    })

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
