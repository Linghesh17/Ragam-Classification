import numpy as np,pickle,pandas as pd
from flask import Flask, render_template, request
app = Flask(__name__)
classifier=pickle.load(open("model.pkl",'rb'))
vector=pickle.load(open("vector.pkl",'rb'))
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confirm", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        l= request.form.get('name')
        if(('Ma' in l)or('ma' in l)):
            return render_template('ma invalid input.html')
        # Ni and Da
        rules=['Sa','Ri','Ga','Pa','Da','Ni',"Sa'","Ri'","Ga'","Pa'","Da'","Ni'","Sa.","Ri.","Ga.","Pa.","Ni.","Da.",'-']
        l1=l.split(' ')
        for i in l1:
            if(i not in rules):
                return render_template('invalid input.html')
        l1=np.array([l])
        l1 = vector.transform(l1)
        n1=pd.DataFrame(l1.toarray(), columns=['da', 'ga', 'ni', 'pa', 'ri', 'sa'])
        prediction=classifier.predict(n1)
        if(prediction==0):
            return render_template('confirm.html',name=l,output='Predicted class:{}'.format('MOHANAM'))
        else:
            return  render_template('confirm.html',name=l,output='Predicted class:{}'.format('HAMSADVANI'))

if __name__ == "__main__":
    app.run(debug=True)