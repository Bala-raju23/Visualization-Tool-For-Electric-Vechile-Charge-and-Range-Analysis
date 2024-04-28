from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return render_template('scafold-2\scaffold-2\index.html')

if__name__ == '__main__';
app.run(debug=true)