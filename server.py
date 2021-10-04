from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "bigboyjiglolyfeproductionzaha.2021"


@app.route('/')
def index():
    session['survey'] = []
    return render_template('index.html')



@app.route('/survey', methods = ['POST'])
def my_surveys():
    
    session['full_name'] = request.form['full_name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment1'] = request.form['comment1']

    return redirect("/results")


@app.route('/results')
def my_results():
    

    return render_template("results.html")







if __name__=="__main__":
    app.run(debug=True)