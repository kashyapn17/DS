
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            potential = float(request.form['potential'])
            preferred_foot = int(request.form['preferred_foot'])
            attacking_work_rate = int(request.form['attacking_work_rate'])
            defensive_work_rate = int(request.form['defensive_work_rate'])
            crossing = float(request.form['crossing'])
            finishing = float(request.form['finishing'])
            heading_accuracy = float(request.form['heading_accuracy'])
            short_passing = float(request.form['short_passing'])
            volleys = float(request.form['volleys'])
            curve = float(request.form['curve'])
            free_kick_accuracy = float(request.form['free_kick_accuracy'])
            long_passing = float(request.form['long_passing'])
            sprint_speed = float(request.form['sprint_speed'])
            agility = float(request.form['agility'])
            reactions = float(request.form['reactions'])
            balance = float(request.form['balance'])
            shot_power = float(request.form['shot_power'])
            jumping = float(request.form['jumping'])
            stamina = float(request.form['stamina'])
            strength = float(request.form['strength'])
            long_shots = float(request.form['long_shots'])
            aggression = float(request.form['aggression'])
            positioning = float(request.form['positioning'])
            vision = float(request.form['vision'])
            penalties = float(request.form['penalties'])
            gk_diving = float(request.form['gk_diving'])
            gk_handling = float(request.form['gk_handling'])
            gk_kicking = float(request.form['gk_kicking'])
            gk_positioning = float(request.form['gk_positioning'])
            gk_reflexes = float(request.form['gk_reflexes'])

            filename = 'model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            scalar = pickle.load(open('scalar_model.pickle','rb'))
            # predictions using the loaded model file
            prediction=loaded_model.predict(scalar.transform([[potential, preferred_foot, attacking_work_rate,defensive_work_rate, crossing, finishing, heading_accuracy,
            short_passing, volleys, curve, free_kick_accuracy,long_passing, sprint_speed, agility, reactions, balance,
            shot_power, jumping, stamina, strength, long_shots,aggression, positioning, vision, penalties, gk_diving,
            gk_handling, gk_kicking, gk_positioning, gk_reflexes]]))
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app