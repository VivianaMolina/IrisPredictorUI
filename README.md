## Iris Species Classifier (Flask & Scikit-learn)

This project implements a simple Machine Learning model for classifying the three species of the Iris dataset (Setosa, Versicolor, Virginica) and exposes it through a simple web interface using the Flask framework.

The user can input the four key flower measurements (sepal and petal length/width), and the application returns the predicted species along with an illustrative image.

## ✨ Features
Classification Model: Uses a RandomForestClassifier from Scikit-learn, trained with the popular load_iris() dataset.

Model Persistence: The trained model is saved as model_iris.pkl using joblib so it can be loaded by the Flask application without retraining.

Web Interface: Minimalist and responsive user interface (using CSS) implemented in Flask.

Visualization: Displays the image of the predicted Iris species.

## 📁 Project Structure
The project has the following file organization:

```
.
├── models/
│   └── model_iris.pkl    # Trained and saved model
├── static/
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   ├── img/
│   │   ├── Setosa.png    # Image for Setosa
│   │   ├── Versicolor.png# Image for Versicolor
│   │   └── Virginica.png # Image for Virginica
├── templates/
│   └── index.html        # HTML template for the interface
├── iris.py               # Script to train the model (Step 1)
├── server.py             # Main Flask application (Step 2)
├── README.md
└── requirements.txt      # List of Python dependencies

```

Important Note: For the application to work correctly, you must include the three Iris species images (Setosa.png, Versicolor.png, Virginica.png) inside the static/ folder.

## 🛠️ Requirements
Ensure you have Python 3.x installed.

Python Dependencies:

flask
scikit-learn
joblib
numpy

You can install all dependencies with the following command:

pip install flask scikit-learn joblib numpy

## 🚀 Installation and Usage
Follow these two steps to get the application running.

Step 1: Train and Save the Model
First, you must run the training script to generate the model_iris.pkl file needed for the web application. This script will create the models/ folder if it doesn't exist.

python iris.py

Upon completion, you should see the message: Model and target names successfully saved to: models/model_iris.pkl

Step 2: Run the Web Application
Once the model has been saved, you can start the Flask server.

python server.py

The server will start in debug mode. Open your web browser and navigate to the following address:

https://www.google.com/search?q=http://127.0.0.1:5000/ or http://localhost:5000/

## 💻 Using the Interface
Enter Parameters: In the interface, enter the numerical values for the four flower characteristics (sepal and petal length/width, in centimeters).

Prediction: Click the "Predict Species" button.

Result: The page will update and show you:

The predicted Iris species (e.g., Setosa).

The image corresponding to the predicted species.

## 🛑 Error Handling
Model Not Found: If you forget to run iris.py, the server.py application will remind you that the model_iris.pkl file is necessary.

Invalid Input: If you enter text or leave a field empty in the web interface, the application will display an error message requesting numerical values.