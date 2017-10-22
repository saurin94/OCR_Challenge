from flask import Flask, render_template, request, redirect, url_for
import webbrowser
app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/image_click_button', methods = ['POST','GET'])
def image_click_button():
	print "in click button"
	result = request.form
	if request.method == 'POST':
		return render_template("clicked.html", something="saurin")
	#return render_template('index.html', something="saurin did it")

app.run(debug=True)

