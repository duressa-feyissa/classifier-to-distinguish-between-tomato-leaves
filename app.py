import os

import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model.keras', compile=False)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
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
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)
        
        img_array = preprocess_image(file_path)
        prediction = model.predict(img_array)
        
        if prediction[0] > 0.6:
            result = "The image is a tomato leaf"
        else:
            result = "The image is not a tomato leaf"
        
        os.remove(file_path)
        return jsonify({"message": result})
    
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
