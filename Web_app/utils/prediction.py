from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import imghdr

def is_image(file):
    """
    Check if the uploaded file is a valid image
    """

    header = file.read(512)
    file.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return False
    return format.lower() in ['jpg', 'png', 'gif', 'bmp']

def predict_intensity(file, model, img_size=(64, 64)):
    """
    Predict the intensity of an image provided as a file-like object

    Paramters:
    - file:
    - model:
    - img_size:

    Returns:
    - prediction:
    """

    try:
        # Read the image file
        img = Image.open(file.stream)
        img = img.convert('RGB')
        img = img.resize(img_size)

        # Convert image to a numpy array
        img_array = img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make prediction
        prediction = model.predict(img_array)
        return prediction[0][0]
    
    except Exception as e:
        print(f"Error in predict_intensity: {e}")
        return None

def scale(grayscale):
    if grayscale >= 170:
        return 0
    if grayscale >= 160:
        return 1
    if grayscale >= 150:
        return 2
    if grayscale >= 140:
        return 3
    if grayscale >= 130:
        return 4
    if grayscale >= 120:
        return 5
    if grayscale >= 110:
        return 6
    if grayscale >= 100:
        return 7
    if grayscale >= 90:
        return 8
    if grayscale >= 80:
        return 9
    return 10