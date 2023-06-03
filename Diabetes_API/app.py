import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
pred_model = pickle.load(open('Diabetes_disease_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data= (np.array(list(data.values())).reshape(1,-1))
    output= pred_model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input= (np.array(data).reshape(1,-1))
    print(final_input)
    output=pred_model.predict(final_input)[0]
    
    if(int(output)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        
    return render_template("result.html",prediction_text="prediction {}".format(output))





if __name__=="__main__":
    app.run(debug=True)
   
     