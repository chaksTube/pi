from flask import Flask, request, send_from_directory, render_template
from . import app
import os
import re



@app.route("/home")
def home():
	data = []
	categories = ['Movies', 'Music', 'Videos']
	image_formats = ['jpg']
	path = os.path.abspath(os.path.dirname(__file__)) + "/static/hdd/"
	print path 
	for path, dirs, files in os.walk(path):
		outer_dict = dict()
		x = path
		if x.split("/")[-1] in categories: 
			print x
			outer_dict['name'] = x.split("/")[-1]
			outer_dict['videos'] = []
			for f in files:
				y = str(f)
				name_underscored = y.split(".")[0]
				if not y.split(".")[1] in image_formats:
					inner_dict = dict()
					inner_dict['name'] = name_underscored.replace('_', ' ')
					inner_dict['path'] = '/static/hdd/' + x.split("/")[-1] + '/'+ y
					inner_dict['thumbnail'] = '/static/hdd/' + x.split("/")[-1] + '/' + y.split(".")[0] + '.jpg'
					outer_dict['videos'].append(inner_dict)
			data.append(outer_dict)

	# print data
	return render_template("index.html", data=data)

@app.route("/single")
def single():
    return render_template("single.html")

@app.route("/sample", methods=['GET'])
def sample():
	url = request.args.get('url', '')
	url = str(url)
	a = url.split("::")
	folder = a[-2]
	file = a[-1]
   	return render_template("sample.html", folder=folder, file=file)