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





top.mainloop()