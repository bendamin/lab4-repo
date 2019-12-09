from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/contact-me')
def contact():
	return render_template('contacts.html')

if __name__ == '__main__':
	app.run()
