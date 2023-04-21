from flask import Flask, render_template,request


app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login" , methods=['GET' , 'POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('index.html')
    else:
        return render_template('auth/login.html')