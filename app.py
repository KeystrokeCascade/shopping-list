from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
file_path = os.path.abspath(os.getcwd()) + '/list.txt'

if not os.path.isfile(file_path):
	open(file_path, 'a').close()

@app.route('/')
def index():
	with open(file_path, 'r') as file:
		list = file.read().splitlines()
	return render_template('index.html', list=list)

@app.route('/add', methods=['POST'])
def add():
	item = request.form['item']
	with open(file_path, 'a') as file:
		file.write(item + '\n')
	return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
	item = request.form['item']
	with open(file_path, 'r+') as file:
		list = file.read().splitlines()
		list.remove(item)
		file.seek(0)
		file.writelines([item + '\n' for item in list])
		file.truncate()
	return redirect(url_for('index'))