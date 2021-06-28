import tensorflow as tf
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
from riceleafdisease.models import *
from keras.models import model_from_json


def modeltrainer(file,obj):
    check = Check.objects.all().first()
    dir_path = 'media/input'
    if check.flag == 'undone':
        train = ImageDataGenerator(rescale = 1/255)
        validation = ImageDataGenerator(rescale = 1/255)

        train_dataset = train.flow_from_directory('test/basedata/training',target_size =(200,200),batch_size =16,class_mode='categorical')
        validation_dataset = validation.flow_from_directory('test/basedata/validation',target_size =(200,200),batch_size =16,class_mode='categorical')

        model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16,(3,3),activation ='relu',input_shape=(200,200,3)),
        tf.keras.layers.MaxPool2D(2,2),
        #
        tf.keras.layers.Conv2D(32,(3,3),activation ='relu'),
        tf.keras.layers.MaxPool2D(2,2),
        #
        tf.keras.layers.Conv2D(64,(3,3),activation ='relu'),
        tf.keras.layers.MaxPool2D(2,2),
        ##
        tf.keras.layers.Flatten(),
        ##
        tf.keras.layers.Dense(512,activation='relu'),
        ##
        tf.keras.layers.Dense(3,activation='softmax'),
        
        ])

        model.compile(loss='categorical_crossentropy',optimizer= tf.keras.optimizers.RMSprop(learning_rate=0.001),metrics=['accuracy'])
        model.fit(train_dataset,steps_per_epoch = 3,epochs=30,validation_data= validation_dataset)
        check.flag = 'done'
        check.save()
        model_json = model.to_json()
        with open("models.json", "w") as json_file:
            json_file.write(model_json)
        model.save_weights("model.h5")

    else:
        json_file = open('models.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        print('i ran tooo very long time ago')
        for i in os.listdir(dir_path):
            if file.url == '/' + dir_path + '/' + i:
                print(" i ran ")
                img= tf.keras.preprocessing.image.load_img(dir_path+'//'+i,target_size=(200,200))
                X = tf.keras.preprocessing.image.img_to_array(img)
                X = np.expand_dims(X,axis=0)
                images = np.vstack([X])
                val = loaded_model.predict(images)
                print(val)
                if val[0][0]==1:
                    obj.disease = "bacterial blight"
                    obj.save()
                elif val[0][1]==1:
                    obj.disease = "brown spot"
                    obj.save()
                else:
                    obj.disease = "leaf smut"
                    obj.save()

    return dir_path

    
    





def classify_image(file,obj):
    dir_path = 'media/input'
    print('i ran tooo very long time ago')
    for i in os.listdir(dir_path):
        if file.url == '/' + dir_path + '/' + i:
            print(" i ran ")
            img= tf.keras.preprocessing.image.load_img(dir_path+'//'+i,target_size=(200,200))
            X = tf.keras.preprocessing.image.img_to_array(img)
            X = np.expand_dims(X,axis=0)
            images = np.vstack([X])
            val = model.predict(images)
            print(val)
            if val[0][0]==1:
                obj.disease = "bacterial blight"
                obj.save()
            elif val[0][1]==1:
                obj.disease = "brown spot"
                obj.save()
            else:
                obj.disease = "leaf smut"
                obj.save()

    return dir_path            