from flask import Flask, request, send_from_directory, render_template, jsonify
from . import app
import os
import re
import serial
import json
import datetime
import serial


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
                    inner_dict['path'] = '/static/hdd/' + \
                        x.split("/")[-1] + '/' + y
                    inner_dict['thumbnail'] = '/static/hdd/' + \
                        x.split("/")[-1] + '/' + y.split(".")[0] + '.jpg'
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


@app.route("/gpsdata", methods=['GET'])
def gpsdata():
    #$GPGGA,021514.000,2232.1799,N,11401.1823,E,1,6,1.25,84.0,M,-2.2,M,,*74
	current_lat = 0
	current_lng = 0
	ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
	while 1:
		data = ser.readline()
		if "$GPGGA" in data:
			splitted_data = data.split(",")
			print "Latitude", float(splitted_data[2]) / 100, "Longitude", float(splitted_data[4]) / 100, "sats used", splitted_data[7]
			current_lat = float(splitted_data[2]) / 100
			current_lng = float(splitted_data[4]) / 100
			break
	data = dict()
	data['lat'] = current_lat
	data['lng'] = current_lng
	data['timestamp'] = datetime.datetime.now().strftime("%d/%m/%y %I:%M %p")

	return jsonify(**data)
