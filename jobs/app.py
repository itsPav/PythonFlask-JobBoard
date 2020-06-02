from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')