from flask import Flask, render_template, request, url_for    
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello World! </h1>"

@app.route('/jinja')
def jinja():
    Title = "Jinja Example!"
    name = "Moid"
    return render_template("jinja.html", name=name, Title=Title)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('submit.html', name=name, email=email)

@app.route('/df')
def df():
    data = {
        "Name" : ['Moid', 'Wasiq', 'Sadiq'],
        "Email" : ['moid.analyst@gmail.com', 'wasiq_s@hotmail.com', 'sadiq@gmail.com']
    }
    df = pd.DataFrame(data)
    df_html = df.to_html(classes='table table-striped', index=False)

    return render_template('df.html', df_html=df_html)

if __name__ == "__main__":
    app.run(debug=True)