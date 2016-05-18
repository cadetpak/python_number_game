import random
from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'X+P@1C#E5e<!LxF7npe8d~Dv3kxMQQ'

def random_number():
	if 'random' not in session:
		session['random'] = int(random.randrange(0,101))
		

@app.route('/')
def index():
	random_number()
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	print "Got It"
	if 'guess' not in session:
		session['guess'] = int(request.form['guess'])
	else: 
		session['guess'] = int(request.form['guess'])

	return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
	if 'random' in session:
		session.pop('random')
	if 'guess' in session:
		session.pop('guess')
	return redirect('/')

app.run(debug=True)
