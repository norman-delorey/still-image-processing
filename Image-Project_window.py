__author__ = 'Norman Delorey'
__version__ = '1.0'
#
#
#This class creates a window to display an image, and contains the options and commands for altering it.
from tkinter import Tk, mainloop, Label, OptionMenu, StringVar, Spinbox, Button
from PIL import Image, ImageTk
from imageProcessing import ImageProcessing

class Window():
    def __init__(self):
        self.root = Tk()
        self.picture = ImageProcessing()
        self.option = StringVar()
        self.option.set("Default")
        self.actions = OptionMenu(self.root, self.option, "Default", "Edge", "Grayscale", "Red Hue", "Green Hue", "Blue Hue",
                                  "Change the Saturation", "White Hue", "Invert Colors", "To French Flag", "Customise")
        self.option.trace('w', self.optionChange)
        self.actions.grid(row=0, column=0)
        self.newPictureButton = Button(self.root, text="New Picture", command=self.changePicture)
        self.newPictureButton.grid(row=0, column=1)
        try:
            self.p = self.picture.getImage()
            self.photo = ImageTk.PhotoImage(self.p)
            self.hValue = Spinbox()
            self.sValue = Spinbox()
            self.vValue = Spinbox()
            self.imageLabel = Label(self.root, image=self.photo)
            self.imageLabel.grid(row=1,column=0,columnspan=15)
            self.root.mainloop()
        except:
            self.root.destroy()



    def optionChange(self, *args):
        """
        This method is called when the user changes options
        :param args:
        :return:none
        """

        self.imageLabel.grid_forget()
        img = self.picture.getImage()
        if self.option.get() == "Default":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = img
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Edge":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.edge(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Grayscale":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toGrayscale(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Red Hue":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toRed(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Green Hue":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toGreen(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Blue Hue":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toBlue(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Change the Saturation":
            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass

            self.contrast = Spinbox(self.root, from_=0.0, to_= 2.0, increment=.1, command=self.updateSaturation)
            self.contrast.grid(row=0,column=2)
            self.updateSaturation()
        elif self.option.get() == "White Hue":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toWhite(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "Invert Colors":
            try:
                self.contrast.grid_forget()
            except:
                pass
            self.p = self.picture.invertColors(img)
            self.photo = ImageTk.PhotoImage(self.p)
        elif self.option.get() == "To French Flag":
            try:
                self.contrast.grid_forget()
            except:
                pass

            try:
                self.hLabel.grid_forget()
                self.hValue.grid_forget()
                self.sLabel.grid_forget()
                self.sValue.grid_forget()
                self.vLabel.grid_forget()
                self.vValue.grid_forget()
            except:
                pass
            self.p = self.picture.toFrenchFlag(img)
            self.photo = ImageTk.PhotoImage(self.p)
        else:
            try:
                self.contrast.grid_forget()
            except:
                pass

            self.hLabel = Label(self.root, text = "Hue:")
            self.hLabel.grid(row=0, column=2)
            self.hValue = Spinbox(from_ = 1.0, to_ = 4.0, increment = .2, command=self.updateHSV)
            self.hValue.grid(row=0, column=3)

            self.sLabel = Label(self.root, text = "Saturation: ")
            self.sLabel.grid(row=0, column=4)
            self.sValue = Spinbox(from_ = 1.0, to_ = 4.0, increment = .2, command=self.updateHSV)
            self.sValue.grid(row=0, column=5)

            self.vLabel = Label(self.root, text = "Value: ")
            self.vLabel.grid(row=0, column=6)
            self.vValue = Spinbox(from_ = 1.0, to_ = 4.0, increment = .2, command=self.updateHSV)
            self.vValue.grid(row=0, column=7)

            self.updateHSV()

        self.imageLabel = Label(self.root, image=self.photo)
        self.imageLabel.grid(row=1, column=0, columnspan=15)

    def updateSaturation(self):
        """
        This is for updating the saturation of the image with the imageProcessing.changeSaturation() method
        :return:
        """
        self.p = self.picture.changeSaturation(self.picture.getImage(), self.contrast.get())
        self.photo = ImageTk.PhotoImage(self.p)
        self.imageLabel = Label(self.root, image=self.photo)
        self.imageLabel.grid(row=1, column=0, columnspan=15)

    def updateHSV(self):
        """
        This updates the image through the imageProcessing.toCustomHSV() method
        :return:
        """
        self.p = self.picture.toCustomHSV(self.picture.getImage(), self.hValue.get(), self.sValue.get(), self.vValue.get())
        self.photo = ImageTk.PhotoImage(self.p)
        self.imageLabel = Label(self.root, image=self.photo)
        self.imageLabel.grid(row=1, column=0, columnspan=15)

    def changePicture(self):
        self.picture.setImage(self.picture.prompt_and_set_file())
        self.imageLabel.grid_forget()
        img = self.picture.getImage()
        self.p = img
        self.photo = ImageTk.PhotoImage(self.p)
        self.imageLabel = Label(self.root, image=self.photo)
        self.imageLabel.grid(row=1, column=0, columnspan=15)


