from app import app
from flask import render_template
from fitbit import step_getter

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/stats')
def stats():
	import locale
	locale.setlocale(locale.LC_ALL, 'en_US')
	steps = step_getter.StepGetter().get_steps_since('2015-08-19')

	return "Steps: " + str(locale.format("%d", steps, grouping=True))