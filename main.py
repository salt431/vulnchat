from flask import Flask, render_template, request, jsonify
from random import randint

web_site = Flask(__name__)

data = []

@web_site.route('/about')
def about():
	num = randint(0, 10000)
	return render_template('about.html', number=num)

@web_site.route('/data/')
def send_test():
	msg = request.args["msg"]
	data.append(msg)
	return jsonify([
{
	"msg": "success",
	"data": data
}
	])
@web_site.route('/')
def index():
	return render_template('index.html', text=data)

@web_site.route('/changelog')
def changelog():
	return render_template('changelog.html')

web_site.run(port=8080)