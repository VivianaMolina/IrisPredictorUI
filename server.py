from flask import Flask, render_template, request, redirect 
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder='static') 
model, target_names = joblib.load('models/model_iris.pkl')

model_path = os.path.join('models', 'model_iris.pkl')

try:
    model, target_names = joblib.load(model_path)
except FileNotFoundError:
    print(f"Model file not found at {model_path}. Please train and save the model first.")
    model, target_names = None, None  # Optional: fallback values or redirect logic

# Map species name to image filename
species_images = {
    'setosa': 'Setosa.png',
    'versicolor': 'Versicolor.png',
    'virginica': 'Virginica.png'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_file = None

    if request.method == 'POST':
        try:
            sl = float(request.form['sepal_length'])
            sw = float(request.form['sepal_width'])
            pl = float(request.form['petal_length'])
            pw = float(request.form['petal_width'])

            input_data = np.array([[sl, sw, pl, pw]])
            pred_index = model.predict(input_data)[0]
            pred_name = target_names[pred_index]

            prediction = pred_name.capitalize()
            image_file = species_images[pred_name.lower()]
        except ValueError:
            prediction = "Invalid input. Please enter numeric values."

    return render_template('index.html', prediction=prediction, image_file=image_file)


if __name__=="__main__":   
    app.run(debug=True)    