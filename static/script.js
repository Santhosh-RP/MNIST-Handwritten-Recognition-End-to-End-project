function previewImage() {
    var file = document.getElementById("image-input").files[0];
    var reader = new FileReader();
    reader.onloadend = function() {
        document.getElementById("image-preview").src = reader.result;
        document.getElementById("image-preview").style.display = 'block';
    }
    if (file) {
        reader.readAsDataURL(file);
    }
}

document.getElementById('upload-form').onsubmit = function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('prediction-result').innerHTML = 'Error: ' + data.error;
        } else {
            document.getElementById('prediction-result').innerHTML = 'Predicted Digit: ' + data.prediction;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('prediction-result').innerHTML = 'Failed to predict the digit. See console for details.';
    });
};
