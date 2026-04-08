from flask import Flask,render_template, request
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv('Cleaned_Car_data.csv')
app=Flask(__name__)

@app.route('/')
def home():
    companies=sorted(car['company'].unique())
    car_model=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html',companies=companies,car_model=car_model,year=year,fuel_type=fuel_type)
@app.route('/predict',methods=['POST'])
def predict():
    company= request.form.get('company')
    car_model = request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    print(company, car_model, year, fuel_type, kms_driven)
    # We add a fake 0 for the Unnamed: 0 column
    prediction = model.predict(pd.DataFrame([[0, company, car_model, year, fuel_type, kms_driven]], 
                                            columns=['Unnamed: 0', 'company', 'name', 'year', 'fuel_type', 'kms_driven']))
    print(prediction)
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug = True)