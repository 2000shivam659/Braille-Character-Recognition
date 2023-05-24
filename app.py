import tensorflow
import numpy as np
from flask import Flask,render_template,jsonify,request
from PIL import Image
from keras.utils import load_img,img_to_array
from tensorflow.keras.models import load_model
from pathlib import Path

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


model=load_model("model.h5")

def predict(images):
    test_image=load_img(images,target_size=(28,28))
    test_image=img_to_array(test_image)
    test_image=np.expand_dims(test_image,axis=0)
    a=np.argmax(model.predict(test_image), axis=1)
    return a

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predcit():
    if 'image' not in request.files:
        return jsonify({'error':'No image found'})
    
    image=request.files['image']
    image_path = Path(app.config['UPLOAD_FOLDER']) / image.filename
    try:
        with image_path.open('wb') as f:
            f.write(image.read())
    except Exception as e:
        return jsonify({'error': 'Failed to save image'})

    output=predict(image_path)
    output = chr(ord('a') + output[0])

    return render_template("index.html",output=output)




if __name__ == '__main__':
    app.run(debug=True)