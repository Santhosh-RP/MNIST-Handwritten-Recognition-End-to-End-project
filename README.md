Handwritten Digit Recognition Web App
This is a web application that recognizes handwritten digits (0–9) using a deep learning model. The app is built with Flask and deployed on Render. Users can upload an image of a digit, and the app predicts the digit displayed in the image.


Features
Digit Prediction: Upload a handwritten digit image, and the app predicts the digit.
Interactive Web Interface: A simple and user-friendly front-end for uploading images and viewing predictions.
Deep Learning Model: Uses a pre-trained deep neural network (mnist_ann_model.h5) trained on the MNIST dataset.
Deployed on Render: Accessible online for testing and demonstration.
![Screenshot (4)](https://github.com/user-attachments/assets/74de991d-c3af-4643-bd58-d2278c0b01de)

How It Works
Upload an Image: Choose a file containing a handwritten digit (e.g., 5.png).
Prediction: The app processes the image and predicts the digit using the loaded ML model.
Output: Displays the prediction directly on the interface.


Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/handwritten-digit-recognition.git
cd handwritten-digit-recognition
Set Up Virtual Environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Access the App: Open http://localhost:5000 in your browser.

Deployment
The app is deployed on Render. Visit the live demo:
Handwritten Digit Recognition App

Technologies Used
Back-End: Flask
Front-End: HTML, CSS, JavaScript
Machine Learning: TensorFlow/Keras
Deployment: Render
