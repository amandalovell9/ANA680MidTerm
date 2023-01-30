from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__)
filename = 'file_student.pkl'
#model = pickle.load(open(filename, 'rb'))
k = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')
def index(): 
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    readingscore = request.form['readingscore']
    writingscore = request.form['writingscore']
    mathscore = request.form['mathscore']
   

    
      
    pred = model.predict(np.array([[ readingscore, writingscore, mathscore]]))
    print(pred)
    return render_template('index.html', predict=str(pred))


if __name__ == '__main__':
    app.run