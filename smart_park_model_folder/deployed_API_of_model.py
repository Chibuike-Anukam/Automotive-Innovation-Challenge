from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np

# Load the trained YOLO model
model = YOLO("runs/detect/train/weights/best.pt")  # Replace with your model path

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Check if a file was uploaded
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Read the uploaded image
    nparr = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform inference
    results = model(image)

    # Extract predictions
    predictions = []
    for result in results:
        for box in result.boxes:
            predictions.append({
                "class": model.names[int(box.cls)],
                "confidence": float(box.conf),
                "bbox": box.xyxy.tolist()  # Convert tensor to list
            })

    return jsonify({"predictions": predictions})

# Run the API
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)