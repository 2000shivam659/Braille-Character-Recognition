from flask import Flask,render_template,redirect
from PIL import Image


app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


if __name__ == '__main__':
    app.run(debug=True)