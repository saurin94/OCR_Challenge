from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
	return render_template('index.html')

@app.route('/image_click_button',methods = ['POST', 'GET'])
def image_click_button():
   if request.method == 'POST':
      result = request.form
      print result
      print "Hello"

app.run(debug=True)

