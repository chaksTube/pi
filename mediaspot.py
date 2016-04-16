from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='/static', instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/home")
def hello():
    return "Hello World!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)