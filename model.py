''' The model.py file is used to display the model on our model page'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from data import get_data

# Load the data
df = get_data()

# Define the features (X) and target (y)
X = df[['HP', 'Attack']]
y = df['Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Define a function to make predictions
def predict_type(hp, attack):
    ''' The predict type makes predictions based on type'''
    prediction = model.predict([[hp, attack]])
    return prediction[0]

# Define a function to evaluate the model
def evaluate_model():
    ''' The evaluate function allows us to test our model and return the accuracy'''
    accuracy = model.score(X_test, y_test)
    return accuracy
