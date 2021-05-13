from flask import Flask, render_template
from classes.Personagem import Personagem

app = Flask(__name__)


@app.route('/')
def route():
	return render_template('index.html',personagem=Personagem)



app.run(debug=True)