import io
import os

import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from PIL import Image
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model.keras', compile=False)

def preprocess_image(img):
    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"message": "No file selected for uploading"}), 400
    
    if file:
        img = Image.open(io.BytesIO(file.read()))
        img_array = preprocess_image(img)
        prediction = model.predict(img_array)
        
        if prediction[0] > 0.6:
            result = "The image is a tomato leaf"
        else:
            result = "The image is not a tomato leaf"
        
        return jsonify({"message": result})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
