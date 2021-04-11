import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl','rb'))
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rishabh.26rr@gmail.com'
app.config['MAIL_PASSWORD'] = 'Rishabh@26'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('I1.html')

@app.route("/predict")
def index():
   msg = Message('Hello', sender = 'rishabh.26rr@gmail.com', recipients = [str(request.form.get("emailId"))])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)


@app.route('/predict',methods=['POST'])
def predict():
    features=[x for x in request.form.values()]
    float_features=[]
    for i in range(0,len(features)-1):
        float_features.append(features[i])
    #float_features = [float(x) for x in len(request.form.values())]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    if output==1:
        return render_template('I1.html', prediction_text="successfull movie")
    else:
        return render_template('I1.html', prediction_text="not a successfull movie")
    
    return render_template('I1.html', prediction_text='{}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    if output==1:
        return jsonify("this is a successfull movie")
    else:
        return jsonify("this is not a successfull movie")

if __name__=="__main__":
    app.run(debug=True)
    


