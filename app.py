from flask import Flask
from flask import render_template

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

app = Flask(__name__)

# default ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def intrernal_server_error(e):
	return render_template('500.html'), 500


# experements ::::::::::::::::::::::::::::::::::::::::::::::::::::::

@app.route('/')
def index():
	return render_template('index.html')


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
	app.run()