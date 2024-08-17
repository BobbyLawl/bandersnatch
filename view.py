''' The view.py file is used to render our data into something visible'''
from flask import render_template, request
from app import app
from model import predict_type, evaluate_model

# Define a route for the homepage
@app.route('/')
def home():
    ''' The home function renders the home.html template'''
    return render_template('home.html')

# Define a route for the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    ''' The predict function predicts various levels based on total level'''
    hp = int(request.form['hp'])
    attack = int(request.form['attack'])
    prediction = predict_type(hp, attack)
    return render_template('view.html', prediction=prediction)

# Define a route for the evaluation page
@app.route('/evaluate')
def evaluate():
    ''' The evaluate function lets us determine the accuracy of the prediction'''
    accuracy = evaluate_model()
    return render_template('model.html', accuracy=accuracy)
