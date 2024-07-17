# # Tomato Leaf or not Classifier

This project is a web application designed to classify whether an uploaded image is a tomato leaf or not using a pre-trained machine learning model. The application utilizes Flask for the backend and a simple HTML front-end.

## Features

- Upload an image and get a classification result.
- Display the selected image immediately upon selection.
- Show a loading spinner while the image is being processed.
- Option to change the image and re-upload.

## Requirements

- Python 3.x
- Flask
- TensorFlow
- PIL (Pillow)

## Live
```bash
    https://classifier-to-distinguish-between-tomato.onrender.com
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tomato-leaf-classifier.git
   cd tomato-leaf-classifier

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required packages:
    ```bash
    pip install -r requirements.txt

4. Ensure you have a trained TensorFlow model saved as model.keras in the project directory.
    ```bash
    python3 app.py

## Usage

  - Navigate to the web application in your browser.
  - Click on "Choose an image" to select an image from your device.
  - The selected image will be displayed immediately.
  - Click on "Upload" to classify the image.
  - The result will be displayed along with an option to change the image.



