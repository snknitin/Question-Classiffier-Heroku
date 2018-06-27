from flask import Flask, request, flash, jsonify, render_template, make_response
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import classify_train as ct
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
	words = TextField('Words:', validators=[validators.required()])


@app.route("/")
def index():
	form = ReusableForm(request.form)
	print(form.errors)
	if request.method == 'POST':
		words = request.form['words']
		print(words)

		if not form.validate():
			flash('All the form fields are required. ')

	return render_template('index.html', form=form)


@app.route("/", methods=['GET', 'POST'])
def predict():
	# # Take data value and get features
	words = request.form['words']
	print(words)

	return "%s\t \n is  %s\t"% (words,ct.is_question(words))


if __name__ == "__main__":
	app.run()