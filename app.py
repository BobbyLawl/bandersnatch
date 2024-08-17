''' The app.py file is used to connect and generate a webpage with Flask'''
from flask import Flask, render_template, request, json
import pandas as pd

app = Flask(__name__)

# Load the data
df = pd.read_csv('monsters.csv')


@app.route('/view', methods=['GET', 'POST'])
def view():
    ''' The view function allows us to see the monster page'''
    try:
        monster_names = df['Name'].unique()
    except KeyError:
        return "Error: 'Name' column not found in the data.", 500

    monster_data = None
    selected_monster = None

    if request.method == 'POST':
        selected_monster = request.form['monster_name']
        print("Monster Name:", selected_monster)
        monster_data = df.loc[df['Name'] == selected_monster]
        print("Monster Data:", monster_data)

        # Sort the results by Level
        monster_data = monster_data.sort_values(by='Level', ascending=True)

        if not isinstance(monster_data, pd.DataFrame):
            monster_data = None

    return render_template('view.html', monster_names=monster_names, monster_data=monster_data, selected_monster=selected_monster)


@app.route('/')
def home():
    ''' The home function renders our template to an html doc'''
    return render_template('home.html')


@app.route('/data')
def data():
    ''' The data function renders our html while dropping columns'''
    data = df.drop(['Unnamed: 0', '_id'], axis=1)
    return render_template('data.html', data=data)


@app.route('/model')
def model():
    ''' The model function renders the necessary time stamp'''
    return render_template('model.html', timestamp="2023-01-16 2:56:47 PM")


@app.route('/predict', methods=['POST'])
def predict():
    ''' The predict function is for the model page to predict rarity'''
    level = int(request.form['level'])

    if level < 20:
        health = 50
        energy = 100
        sanity = 60
        rarity = "Rank 1"
        confidence = 20
    elif level < 50:
        health = 70
        energy = 120
        sanity = 70
        rarity = "Rank 2"
        confidence = 30
    elif level < 70:
        health = 90
        energy = 140
        sanity = 80
        rarity = "Rank 3"
        confidence = 40
    else:
        health = 110
        energy = 160
        sanity = 90
        rarity = "Rank 4"
        confidence = 50

    result = {
        "level": level,
        "health": health,
        "energy": energy,
        "sanity": sanity,
        "rarity": rarity,
        "confidence": confidence
    }

    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True)
