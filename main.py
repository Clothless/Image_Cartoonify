# Importing what we need
import tkinter as tk  	# It is a Python binding to the Tk GUI toolkit
from tkinter import *
import easygui  		# EasyGUI is a module for very simple, very easy GUI programming in python
import cv2  			# This is a module from the OpenCV library, it will be used for the image processing
import matplotlib.pyplot as plt #This library is used for visualization and plotting. Thus, it is imported to form the plot of images
import os  				# For OS interaction. Here, to read the path and save images to that path
import sys			# This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter


# Making the GUI main window
top = tk.Tk()
top.geometry('400x400')
top.title('Image Cartoonify !')
top.configure(background='#0f2c33')
label = Label(top, background='#CDCDCD', font=('calibri', 20, 'bold'))


# fileopenbox Function opens the box to choose file and help us store file path as string
# fileopenbox() is a method from easyGUI module and it returned a string for the path chosen
def upload():
    image_path = easygui.fileopenbox()
    cartoonify(image_path)


# This is all about the button creation, calling of upload function, setting background, font, and other specifications
upload = Button(top, text="Cartoonify an Image", command=upload, padx=10, pady=5)
upload.configure(background="#374256", foreground="wheat", font=('calibri', 10, 'bold'))
upload.pack(side=TOP, pady=50)


# This code makes a button when the picture is transformed. It gives an alternative to save the cartoonified picture
savel = Button(top, text="Save cartoon image", command=lambda: save(resize_image6, image_path), padx=30, pady=5)
savel.configure(background="#364156", foreground="white", font=("calibri", 10, "bold"))
savel.pack(side=TOP, pady=50)


# Storing the Image
def cartoonify(image_path):
	# Read image
	# Imread is a method in cv2 which is used to store images in the form of numbers
	original_image = cv2.imread(image_path)
	original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
	print(original_image) # this will be stored in form of number

	# To confirm if it is an image that was chosing
	if original_image is None:
		print("Can’t find any image! Choose appropriate file. ")
		sys.exit()
	# Resize the image after each transformation
	# We resize the image after each transformation to display all the images on a similar scale at last
	resize_image1 = cv2.resize(original_image, (960, 540))
	plt.imshow(resize_image1, cmap='gray')

	# Transform Image to grayscale
	# Our first step is to convert the image into grayscale
	grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
	# cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’
	# we use the BGR2GRAY flag. This returns the image in grayscale

	# After each transformation, we resize the resultant image using the resize() method in cv2
	# This is done to get more clear insights into every single transformation step
	resize_image2 = cv2.resize(grayscale_image, (960, 540))
	# And display it using imshow() method
	plt.imshow(resize_image2, cmap="gray")

	# Smoothening a grayscale image
	smooth_grayscale_image = cv2.medianBlur(grayscale_image, 5)
	# The medianBlur() function from cv2 is used in smoothening the grayscale image
	resize_image3 = cv2.resize(smooth_grayscale_image, (960, 540))
	plt.imshow(resize_image3, cmap="gray")

	# Extracting the edges in the image
	# Retrieving the edges for cartoon effect
	get_edge = cv2.adaptiveThreshold(smooth_grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	resize_image4 = cv2.resize(get_edge, (960, 540))
	plt.imshow(resize_image4, cmap="gray")

	# Smooth Colours
	# Applying bilateral filter to remove noise
	color_image = cv2.bilateralFilter(original_image, 9, 300, 300)
	resize_image5 = cv2.resize(color_image, (960, 540))
	plt.imshow(resize_image5, cmap="gray")

	# Giving a Cartoon Effect
	# Masking edged image with our “BEAUTIFY” image
	cartoon_image = cv2.bitwise_and(color_image, color_image, mask=get_edge)
	resize_image6 = cv2.resize(cartoon_image, (960, 540))
	plt.imshow(resize_image6, cmap="gray")

top.mainloop()

