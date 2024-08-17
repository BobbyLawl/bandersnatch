from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.utils import shuffle
import numpy as np

df = pd.read_html('C:\\Users\\Bobby\\Desktop\\bloomfp\\monsters.html', header=0)[0]
df = df.drop('_id', axis=1)  # Drop the _id column
df.set_index('Name', inplace=True)  # Set the Name column as the index

X = df.drop('Weakness', axis=1)  # Features
y = df['Weakness']  # Target

app = Flask(__name__)

# Create the SGDClassifier model
model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3)

# Define the batch size
batch_size = 1000

# Train the model in batches
for i in range(0, len(X), batch_size):
    X_batch, y_batch = X[i:i+batch_size], y[i:i+batch_size]
    X_batch, y_batch = shuffle(X_batch, y_batch)
    model.partial_fit(X_batch, y_batch, classes=np.unique(y))

# Define a function to make predictions
def make_prediction(data):
    prediction = model.predict(data)
    return prediction

# Define a route for the API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = make_prediction(df)
    return jsonify({'prediction': prediction.tolist()})

# Define a route for the root URL
@app.route('/')
def index():
    return "Welcome to the monster prediction API!"

if __name__ == '__main__':
    # Save the trained model to a new file
    joblib.dump(model, 'new_model.pkl')
    print("New model saved to new_model.pkl")
    app.run(debug=True)