__author__ = 'Sudheer'
import imghdr
import tkMessageBox
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename

from PIL import Image, ImageTk

from moments import plot
from config import result_values_file
import definitions


def open_file_explorer():
    filename = askopenfilename()
    image_type = imghdr.what(filename)
    if filename and image_type == "png" or image_type == "jpg":
        result_values_file.filename = filename
        plot.zernike_moments_for_all_angles()
        image_description_window()
    else:
        tkMessageBox.showerror("No Image Selected", "Please select an Image")


def main_window():
    try:
        master = Tk()
        master.title("Pokedex")
        master.minsize(500, 500)
        master.maxsize(500, 500)
        intro_label = Label(master,
                            text=definitions.pokedex_intro,
                            font=12, wraplength=500)
        intro_label.pack()
        description_string = StringVar()
        description_string.set(definitions.image_moment_definition)
        description_label = Label(master, textvariable=description_string, wraplength=500)
        description_label.pack()
        hu_moment_description = StringVar()
        hu_moment_description.set(definitions.hu_moment)
        hu_moments_label = Label(master, textvariable=hu_moment_description, wraplength=500)
        hu_moments_label.pack()
        zernike_moment_description = StringVar()
        zernike_moment_description.set(definitions.zernike_moment)
        zernike_moments_label = Label(master, textvariable=zernike_moment_description, wraplength=500)
        zernike_moments_label.pack()
        buttons_frame = Frame(master)
        buttons_frame.pack(side=BOTTOM)
        upload_button = Button(buttons_frame, text="Upload Image", command=open_file_explorer, height=3, width=10)
        upload_button.pack()
        close_button = Button(buttons_frame, text="Close", command=master.destroy, height=3, width=10)
        close_button.pack()
        master.mainloop()
    except Exception as e:
        raise RuntimeError, e


def image_description_window():
    try:
        image_window = Toplevel()
        canvas = Canvas(image_window, width=300, height=300)
        canvas.pack()
        image = Image.open(result_values_file.filename)
        object_image = ImageTk.PhotoImage(image)
        canvas.create_image(150, 150, image=object_image)
        if result_values_file.result:
            canvas.create_text(150, 200, text="The Object Identified is: " + result_values_file.result)
        else:
            canvas.create_text(150, 200, text="Object successfully stored in Database ")
        buttons_frame = Frame(image_window)
        buttons_frame.pack(side=BOTTOM)
        rotate_image_button = Button(buttons_frame, text="Rotate Image",
                                     command=plot.plot_outline_for_all_angles)
        rotate_image_button.pack()
        close_button = Button(buttons_frame, text="Close", command=image_window.destroy, height=2, width=5)
        close_button.pack()
        image_window.mainloop()
    except Exception as e:
        raise RuntimeError, e
