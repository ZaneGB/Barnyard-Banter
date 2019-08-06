#*******************************************************************
#BARNYARD BANTER APP
#*******************************************************************
#Import Libraries
from flask import Flask, render_template, url_for, request
import keras
from keras.models import load_model
import h5py
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras import applications
import tensorflow as tf
import urllib.request
import re
from random import random

# import urllib2

#-------------------------------------------------------------------

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/choose',methods=['GET'])
def choose():
    # np.random.seed(50)
    index = np.random.randint(50)

    return render_template("choose.html", index=index)

@app.route('/value/<imgname>',methods=['GET', 'POST'])
def predict_api(imgname):
    keras.backend.clear_session() 
    graph = tf.get_default_graph()
    with graph.as_default():
        model = load_model('model/image_model_trained.h5')
    vgg16 = applications.VGG16(include_top=False, weights='imagenet')
    path = 'static/test/'+imgname

    image = load_img(path, target_size=(224, 224))  
    image = img_to_array(image)  
    image = np.expand_dims(image, axis=0)
    image /= 255.

    animals = ['cat', 'cow', 'dog', 'sheep']

    with graph.as_default():
        bt_prediction = vgg16.predict(image) 
        class_predicted = model.predict_classes(bt_prediction)
    output = animals[class_predicted[0]]

    return render_template("results.html", animal=output, pic="../"+path)

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        print(request.form['exp'])
        picnm = request.form['exp']
        keras.backend.clear_session() 
        graph = tf.get_default_graph()
        with graph.as_default():
            model = load_model('model/image_model_trained.h5')
        vgg16 = applications.VGG16(include_top=False, weights='imagenet')
        match = re.search('^http', picnm)
        if match:
            rnd = random()
            print ('found', match.group()) ## 'found word:cat'
            path = 'static/test/_Uploaded_Img'+str(rnd)+'.jpg'
            urllib.request.urlretrieve(picnm, path)
        else:
            print ('did not find')
            path = 'static/test/'+picnm
        print(match)
        print(picnm)

        # filedata = urllib2.urlopen(picnm)
        # datatowrite = filedata.read()
        
        # with open('/static/test/cat1002.jpg', 'wb') as f:
        #     f.write(datatowrite)        
        # path = 'static/test/'+picnm
        image = load_img(path, target_size=(224, 224))  
        image = img_to_array(image)  
        image = np.expand_dims(image, axis=0)
        image /= 255.

        animals = ['cat', 'cow', 'dog', 'sheep']

        with graph.as_default():
            bt_prediction = vgg16.predict(image) 
            class_predicted = model.predict_classes(bt_prediction)
        output = animals[class_predicted[0]]
    
        return render_template("results.html", animal=output, pic=path)

if __name__ == "__main__":
    app.run(debug=True)

#*******************************************************************