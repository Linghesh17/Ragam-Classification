import pickle
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request
app = Flask(__name__)
classifier=pickle.load(open("model.pkl",'rb'))
@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confirm", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        l= request.form.get('name')
        n = [l]
        edata=LabelEncoder()
        n=edata.fit_transform(n)
        n=n.reshape(-1,1)
        prediction=classifier.predict(n)
        if(prediction==0):
            return render_template('confirm.html',name=l,output='Predicted class:{}'.format('HAMSADVANI'))
        else:
            return  render_template('confirm.html',name=l,output='Predicted class:{}'.format('MOHANAM'))

if __name__ == "__main__":
    app.run(debug=True)