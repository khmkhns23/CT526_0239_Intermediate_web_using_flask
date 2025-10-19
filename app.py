from flask import Flask, render_template, request, jsonify
from mylib import myfunct

app = Flask(__name__)

@app.route('/')
def home():
    # You can pass variables into the template
    name = "Yut"
    return render_template('index.html', name=name)

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/draw/<int:s>')
def draw(s):
    # print("-" * 50)
    texthtml = ""
    for i in range(1,s+1):
        texthtml += (myfunct("Hi!", i)) +"<br>"  
    # return texthtml
    return render_template('draw.html',count=s,textto='OK',txt = texthtml)

@app.route('/myid')
def myid():
    data = '68130239'
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    user_text = request.form.get('user_text')
    return render_template('index.html', name="Yut", message=f"You entered: {user_text}")

@app.route('/sum/<xx>/<yy>')
def sums(xx, yy): 
    try:
        value1 = int(xx)
        value2 = int(yy)
        zz = value1 + value2
        returnto = "The result of sum between "+ str(value1) +" and " + str(value2) + " is "+ str(zz) +""
    except ValueError:
        returnto = "You are using miss data type for operation"

    # return str(returnto)  # ✅ must return string
    return render_template('results.html',returnto = returnto)

@app.route('/concat/<xx>/<yy>')
def concats(xx, yy): 
    try:
       
        value1 = str(xx)
        value2 = str(yy)
        zz = value1 + value2
        returnto = "The result of cancatenate between "+ str(value1) +" and " + str(value2) + " is "+ str(zz) +""
    except ValueError:
        returnto = "You are using miss data type for operation"

    # return str(returnto)  # ✅ must return string
    return render_template('results.html',returnto = returnto)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)

