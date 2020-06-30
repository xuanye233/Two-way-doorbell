# -*- coding: UTF-8 -*-   
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
import requests
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
   return render_template('index.html')


@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        #base_path = os.path.abspath(os.path.dirname(__file__))
        f.save('static/uploads/1.mp3')
    return render_template('index.html')


@app.route('/upload1',methods=['POST'])
def uploads():
    if request.method == 'POST':
        f = request.files.get('file1')
        #base_path = os.path.abspath(os.path.dirname(__file__))
        f.save('static/uploads/2.mp3')
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
