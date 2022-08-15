
import tkinter as tk
from tkinter.constants import ANCHOR
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
from tkinter import filedialog
import cv2
import numpy as np

def yellowButton_callback():
    opencvImage =cv2.cvtColor(np.array(originalImage),cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 0] = 20
    global outputImage
    outputImage= Image.fromarray(cv2.cvtcolor(opencvImage,cv2.color_BGR2RGB))
    displayImage(outputImage)

def blueButton_callback():
    opencvImage =cv2.cvtColor(np.array(originalImage),cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 2] = 100
    global outputImage
    outputImage= Image.fromarray(cv2.cvtcolor(opencvImage,cv2.color_BGR2RGB))
    displayImage(outputImage)

def pinkButton_callback():
    opencvImage =cv2.cvtColor(np.array(originalImage),cv2.COLOR_RGB2BGR)
    opencvImage[:, :, 1] = 100
    global outputImage
    outputImage= Image.fromarray(cv2.cvtcolor(opencvImage,cv2.color_BGR2RGB))
    displayImage(outputImage)

def noneButton_callback():
    pass

def displayImage(displayImage):
    ImagetoDisplay = displayImage.resize((800,500), Image.ANTIALIAS)
    ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
    showWindow.config(image=ImagetoDisplay)
    showWindow.photo_ref = ImagetoDisplay
    showWindow.pack()

def importButton_callback():
    global originalImage
    filename= filedialog.askopenfilename()
    originalImage = Image.open(filename)
    displayImage(originalImage)

def saveButton_callback():
    savefile = filedialog.asksaveasfile(defaultextension='.jpg')
    outputImage.save(savefile)

def closeButton_callback():
    window.destroy()

def brightness_callback(brightness_pos):
    brightness_pos = float(brightness_pos)
    print(brightness_pos)
    global outputImage
    enhancer = ImageEnhance.Brightness(originalImage)
    outputImage = enhancer.enhance(brightness_pos)
    displayImage(outputImage)

def contrast_callback(contrast_pos):
    contrast_pos = float(contrast_pos)
    print(contrast_pos)
    global outputImage
    enhancer = ImageEnhance.Contrast(originalImage)
    outputImage = enhancer.enhance(contrast_pos)
    displayImage(outputImage)

def color_callback(color_pos):
    color_pos = float(color_pos)
    print(color_pos)
    global outputImage
    enhancer = ImageEnhance.Color(originalImage)
    outputImage = enhancer.enhance(color_pos)
    displayImage(outputImage)

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("IMAGE EDITOR")
window["background"] = '#0000FF'
window.geometry(f'{screen_width}x{screen_height}')
Frame1 = tk.Frame(window, height = 20, width=screen_width)
Frame1.pack(anchor=tk.NW)

Frame2 = tk.Frame(window, height=20)
Frame2.pack(anchor=tk.NW)

Frame3 = tk.Frame(window, height=20)
Frame3.pack(anchor=tk.N)

welcome = tk.Label(Frame1, text="welcome to ur image editor",font=("ariel 12 bold"),pady=5, padx=407, bg="#0000FF")
welcome.grid(row=0, column=2)
importButton = tk.Button(Frame1, bg="#0000FF",text="Import",padx=10, pady=5, command=importButton_callback)
importButton.grid(row=0, column=0)



saveButton = tk.Button( Frame1, bg="#0000FF",text="Save",padx=10, pady=5, command=saveButton_callback)
saveButton.grid(row=0,column=1)

closeButton = tk.Button( Frame1, bg="#0000FF",text="Save",padx=10, pady=5, command=closeButton_callback)
closeButton.grid(row=0,column=3)

brightnessSlider = tk.Scale( Frame2, bg="#000000", fg="black",troughcolor="#000000",label="brightness",from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
resolution=0.1, command=brightness_callback )
brightnessSlider.set(1)
brightnessSlider.pack(anchor=tk.N)


contrastSlider = tk.Scale(Frame2,bg="#000000", fg="black",troughcolor="#000000",label="contrast",from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
resolution=0.1, command=contrast_callback)
contrastSlider.set(1)
contrastSlider.pack(anchor=tk.N)

colorSlider = tk.Scale(Frame2,bg="#000000", fg="black",troughcolor="#000000",label="Sturation",from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
resolution=0.1, command=color_callback)
colorSlider.set(1)
contrastSlider.pack(anchor=tk.N)

yellowButton=tk.Radiobutton(Frame3,bg="#FFFF00",text="yellow filter",font=("ariel 10 bold"),width=30, value=1, command=yellowButton_callback)
yellowButton.grid(row=0,column=0)

blueButton=tk.Radiobutton(Frame3,bg="#0000FF",text="blue filter",font=("ariel 10 bold"),width=30, value=2, command=blueButton_callback)
blueButton.grid(row=0,column=1)

pinkButton=tk.Radiobutton(Frame3,bg="#FFC0CB",text="pink filter",font=("ariel 10 bold"),width=30, value=3, command=pinkButton_callback)
pinkButton.grid(row=0,column=2)

noneButton=tk.Radiobutton(Frame3,bg="#FFFFFF",text="white",font=("ariel 10 bold"),width=30, value=4, command=noneButton_callback)
noneButton.grid(row=0,column=3)
noneButton.select()

showWindow = tk.Label(window)
showWindow.pack()
tk.mainloop()




