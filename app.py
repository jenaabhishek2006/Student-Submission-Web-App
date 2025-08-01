from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('form.html')



@app.route('/result', methods = ['POST','GET']) 
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('output.html', result = result)
    else:
        return "Please submit the form from the homepage."
    
app.run(debug=True)