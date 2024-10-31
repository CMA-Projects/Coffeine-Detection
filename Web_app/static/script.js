// Get references to HTML elements
const uploadForm = document.getElementById('uploadForm');
const imageInput = document.getElementById('imageInput');
const resultDiv = document.getElementById('result');
const result2Div = document.getElementById('result2');
const imagePreviewDiv = document.getElementById('imagePreview');

// Handle form submission
uploadForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData();
    const file = imageInput.files[0];
    if (!file) {
        alert('Please select an image to upload.');
        return;
    }
    formData.append('image', file);

    // Clear previous result and show processing message
    resultDiv.innerHTML = 'Processing...';
    resultDiv.innerHTML = '';

    // Display the uploaded image
    const reader = new FileReader();
    reader.onload = function(event) {
        imagePreviewDiv.innerHTML = `<img src="${event.target.result}" alt = "Uploaded Image" style="max-width: 300px; max-height: 300px;" />`
    };
    reader.readAsDataURL(file);

    // Send the image via Fetch API to the backend
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const predictionInt = parseInt(data.prediction_scaled, 10);
            resultDiv.innerHTML = `Predicted Intensity: ${data.prediction}`;
            result2Div.innerHTML = `Predicted Scale: ${predictionInt}`;
        } else {
            resultDiv.innerHTML = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = 'An error occurred while processing the image.';
    });
});
