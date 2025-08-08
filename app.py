from flask import Flask, render_template
from bob.bob import load_params, make_prediction 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("mnist.html")


if __name__ == '__main__':
    app.run(debug=True)