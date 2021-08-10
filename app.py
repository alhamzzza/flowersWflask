from logging import setLoggerClass
from flask import Flask , render_template , request
import pickle
import requests



app = Flask(__name__)
model = pickle.load(open('rfcModel.pkl' , 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route('/predict' , methods = ['POST' ,'GET'])
def predict():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width=float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width=float(request.form['petal_width'])


        prediction=model.predict([[sepal_length	,sepal_width ,	petal_length,	petal_width	 ]])
        if prediction ==0:
                return render_template('index.html',prediction_text="it's Setosa" , info_f = "more about Setosa ?")
        elif prediction == 1:
                return render_template('index.html',prediction_text="it's Versicolor" , info_f = "more about Versicolor ?")
        elif prediction == 2:
                return render_template('index.html',prediction_text="it's Virginica" , info_f = "more about Virginica ?")
        else:
                return render_template('index.html',prediction_text="hata olustu")
         

    else:
        return render_template('index.html')


@app.route('/about',methods=['POST'])
def About():
    return render_template('flowersGallery.html')






if __name__=="__main__":
    app.run(debug=True)