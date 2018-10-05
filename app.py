from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

app.run(host='localhost', port=5000, debug=True)

# 108601642750985747007
# 108601642750985747007