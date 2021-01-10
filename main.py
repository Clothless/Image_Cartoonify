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





top.mainloop()