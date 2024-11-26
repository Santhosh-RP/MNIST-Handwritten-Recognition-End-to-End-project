from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

try:
    model = load_model('models/mnist_ann_model.h5')
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model: {e}")

def prepare_image(image_file):
    try:
        image = Image.open(image_file.stream).convert('L')
        image = image.resize((28, 28), Image.Resampling.LANCZOS)
        img_array = np.array(image)
        img_array = img_array.flatten()
        img_array = img_array.reshape(1, 784)
        img_array = img_array.astype('float32') / 255.0
        return img_array
    except Exception as e:
        logging.error("Failed to process image: {}".format(e))
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        image_file = request.files['image']
        processed_image = prepare_image(image_file)
        if processed_image is not None:
            prediction = model.predict(processed_image)
            predicted_digit = np.argmax(prediction)
            return jsonify({'prediction': int(predicted_digit)})
        else:
            return jsonify({'error': 'Failed to process image'}), 400
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
