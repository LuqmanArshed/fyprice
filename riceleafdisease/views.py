from django.shortcuts import render,redirect
from .models import *
# Create your views here.
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2

from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import tensorflow as tf

from .forms import *

from predictor import *




def logoutuser(request):
	logout(request)
	return redirect('home')






def login_page(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('user_home')
		else:
			messages.info(request,'User or Password is Incorrect')

	context={}
	return render(request,'pages/login.html',context)





def signup(request):
    # train = ImageDataGenerator(rescale = 1/255)
    # validation = ImageDataGenerator(rescale = 1/255)
    # train_images = Training.objects.all()
    # direc = "dataset/basedate/training"
    # train_dataset = train.flow_from_directory(direc,target_size =(200,200),batch_size =16,class_mode='categorical')
    # print(train_dataset)
    context={}
    return render(request,'pages/signupuzi.html',context)






def home(request):
    # train = ImageDataGenerator(rescale = 1/255)
    # validation = ImageDataGenerator(rescale = 1/255)
    # train_images = Training.objects.all()
    # direc = "dataset/basedate/training"
    # train_dataset = train.flow_from_directory(direc,target_size =(200,200),batch_size =16,class_mode='categorical')
    # print(train_dataset)
    
    context={}
    return render(request,'pages/home.html',context)




def trainmodel(request):
    modeltrainer()
    return redirect('home')
    




def upload_image(request):
    form = image_form(initial={'disease':'none'})
    if request.method == 'POST':
        form = image_form(request.POST,request.FILES)
        files = request.FILES.getlist('disease_image')
        if form.is_valid():
            obj=form.save()
            for image in files:
                obj.image = image
                obj.save()
            modeltrainer(obj.image,obj)   
            return redirect('home')
        

    context = {'form':form}
    return render(request, 'pages/upload_image.html', context)