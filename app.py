from flask import Flask, request,app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('/config/workspace/Model/modelforprediction.pkl','rb'))
scaler = pickle.load(open('/config/workspace/Model/standardScaler.pkl','rb'))



## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET','POST'])
def predict_datapoint():
    RESULT = " "
    if request.method == 'POST':
        Pregnancies=float(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data = scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        result = model.predict(new_data)

        if predict[0]==1:
            result = "Diabetic"
        else:
            result = "Non-Diabetic"


        return render_template('single_prediction.html',result = result)
    
    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)


