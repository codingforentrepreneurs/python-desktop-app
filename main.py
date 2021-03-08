from dataclasses import dataclass # pip install dataclasses
import pathlib
import jinja2
import json
from flask import Flask, render_template, request, send_from_directory
import webview # pip install pywebview
from src.api import API

app = Flask(__name__, static_folder='./assets', template_folder='./templates')

@app.route("/")
def home():
    return render_template("home.html", context={"name": "PyDesktop App"}) 

@app.route("/static/")
def serve_static():
    path_arg = request.args.get('path') # ?path=
    if path_arg:
        abs_path = pathlib.Path(path_arg).resolve()
        if abs_path.exists():
            file_dir = abs_path.parent
            file_name = abs_path.name
            return send_from_directory(file_dir, file_name)
    return render_template("home.html", context={"name": "PyDesktop App"}) 

if __name__ == "__main__":
    js_api = API(name='Justin')
    window_args = {
        "js_api": js_api,
        "width": 1200
    }
    window = webview.create_window("PyDesktop", app, **window_args)
    js_api._window = window
    webview.start(debug=True)