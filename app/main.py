'''importing Flask and other modules'''
from flask import Flask, request, render_template
from joblib import load



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/result')
def result():
  return render_template('result.html')


# load the model
model = load("models/model_v1.joblib")


@app.route('/', methods=["GET", "POST"])
def prediction():
    '''
    This will get data from html form and will do prediction.

    Returns
    -------
    html
        html code for render
    '''
    form_items = ['Age', 'SystolicBP', 'DiastolicBP', 'BS',	'BodyTemp', 'HeartRate']
    data = []
    pred = None

    if request.method == "POST":
        # getting input with name = fname in HTML form
        for item in form_items:
            try:
                temp = request.form.get(item)
                temp = temp.strip()
                temp = float(temp)
                data.append(temp)
            except Exception as ex:
                print(ex)
        print(data)
        pred = model.predict([data])
        if pred[0] == 0:
            pred = "high risk 😥. Please Contact Your Doctor 👨‍⚕️"
        elif pred[0] == 1:
            pred = "Low risk 👍"
        elif pred[0] == 2:
            pred = "Mid risk. "

    return render_template("result.html", result=pred)


if __name__ == '__main__':
    app.debug = True
    app.run()
