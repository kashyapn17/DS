
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
            Age = int(request.form['Age'])
            Total_Bilirubin = float(request.form['Total_Bilirubin'])
            Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
            Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
            Total_Protiens = float(request.form['Total_Protiens'])
            Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])
            Female = int(request.form['Female'])
            Male = int(request.form['Male'])
            filename = 'finalmodel.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Age,Total_Bilirubin,Alkaline_Phosphotase,Aspartate_Aminotransferase,Total_Protiens,
                                              Albumin_and_Globulin_Ratio,Female,Male]])
            print('prediction is',prediction[0])
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

@app.route('/from_postman',methods=['POST'])
def from_postman():
    Age = int(request.json['Age'])
    Total_Bilirubin = float(request.json['Total_Bilirubin'])
    Alkaline_Phosphotase = int(request.json['Alkaline_Phosphotase'])
    Aspartate_Aminotransferase = int(request.json['Aspartate_Aminotransferase'])
    Total_Protiens = float(request.json['Total_Protiens'])
    Albumin_and_Globulin_Ratio = float(request.json['Albumin_and_Globulin_Ratio'])
    Female = int(request.json['Female'])
    Male = int(request.json['Male'])
    filename = 'finalmodel.pickle'
    loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
    # predictions using the loaded model file
    prediction = loaded_model.predict(
        [[Age, Total_Bilirubin, Alkaline_Phosphotase, Aspartate_Aminotransferase, Total_Protiens,
          Albumin_and_Globulin_Ratio, Female, Male]])
    print('prediction is',prediction[0])
    return jsonify({'Prediction':prediction[0]})



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app