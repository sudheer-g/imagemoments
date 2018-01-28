__author__ = 'Sudheer'
from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename

from PIL import Image, ImageTk

import main_controller
import result_values_file


def open_file_explorer():
    result_values_file.filename = askopenfilename()
    if(result_values_file.filename):
        print "Hit"
        main_controller.zernike_moments_for_all_angles()
        image_description_window()


def main_window():
    master = Tk()
    master.title("Pokedex")
    master.minsize(500, 500)
    master.maxsize(500, 500)
    intro_label = Label(master,
                        text="Identify any object in a Dataset via Image Recognition through Image Moments.\n\n",
                        font=12, wraplength=500)
    intro_label.pack()
    description_string = StringVar()
    description_string.set(
        "In image processing, computer vision and related fields, an image moment is a certain particular weighted average moment of the image pixels' intensities, or a function of such moments, usually chosen to have some attractive property or interpretation.Image moments are useful to describe objects after segmentation. Simple properties of the image which are found via image moments include area (or total intensity), its centroid, and information about its orientation.\n\n")
    description_label = Label(master, textvariable=description_string, wraplength=500)
    description_label.pack()
    hu_moment_description = StringVar()
    hu_moment_description.set(
        "Hu Moments which are can be used to describe, characterize, and quantify the shape of an object in an image.Hu Moments are normally extracted from the silhouette or outline of an object in an image. By describing the silhouette or outline of an object, we are able to extract a shape feature vector (i.e. a list of numbers) to represent the shape of the object.We can then compare two feature vectors using a similarity metric or distance function to determine how similar the shapes are.\n\n")
    hu_moments_label = Label(master, textvariable=hu_moment_description, wraplength=500)
    hu_moments_label.pack()
    zernike_moment_description = StringVar()
    zernike_moment_description.set(
        "Zernike moments are used to describe the shape of an object; however, since the Zernike polynomials are orthogonal to each other, there is no redundancy of information between the moments.")
    zernike_moments_label = Label(master, textvariable=zernike_moment_description, wraplength=500)
    zernike_moments_label.pack()
    buttons_frame = Frame(master)
    buttons_frame.pack(side=BOTTOM)
    upload_button = Button(buttons_frame, text="Upload Image", command=open_file_explorer, height=3, width=10)
    upload_button.pack()
    close_button = Button(buttons_frame, text="Close", command=master.destroy,height=3, width=10)
    close_button.pack()
    master.mainloop()


def image_description_window():
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
                                 command=main_controller.print_outline_for_all_angles)
    rotate_image_button.pack()
    close_button = Button(buttons_frame, text="Close", command=image_window.destroy, height=2, width=5)
    close_button.pack()
    image_window.mainloop()



if __name__ == "__main__":
    main_window()
    sys.exit(0)
