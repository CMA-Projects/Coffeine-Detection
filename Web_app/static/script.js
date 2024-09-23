// Get references to HTML elements
const uploadForm = document.getElementById('uploadForm');
const imageInput = document.getElementById('imageInput');
const resultDiv = document.getElementById('result');

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

    // Send the image via Fetch API to the backend
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            resultDiv.innerHTML = `Predicted Intensity: ${data.prediction}`;
        } else {
            resultDiv.innerHTML = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = 'An error occurred while processing the image.';
    });
});
