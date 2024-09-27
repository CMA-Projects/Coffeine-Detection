from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from utils.prediction import predict_intensity, is_image
import numpy as np
import io

app = Flask(__name__)

# Load the model
print(f"Loading model...")
model = load_model('models/cnn_model_v2.h5')
print(f"Model loaded successfully!")


# Define the target image size per model's requirement
TARGET_SIZE = (64, 64)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image part in the request'})
    
    file = request.files['image']

    if file.filename == '':
        return jsonify({'success': False, 'error': 'No image selected for uploading.'})
    
    # if not is_image(file):
    #     return jsonify({'success': False, 'error': 'Uploaded file is not a valid image.'})
    
    try:
        result = predict_intensity(file, model, img_size=TARGET_SIZE)

        if result is not None:
            return jsonify({
                'success': True,
                'prediction': f"{result:.2f}"
            })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)