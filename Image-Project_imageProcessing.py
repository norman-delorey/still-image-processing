__author__ = 'Norman Delorey'
__version__ = '1.0'
#
#This file contains the ImageProcessing class. This class makes changes to an image and returns a new version.
from PIL import Image
import colorsys
from tkinter import  filedialog

class ImageProcessing:
    def __init__(self):
        self.imageChosen = self.prompt_and_set_file()

    def prompt_and_set_file(self):
        """prompt the user to open a file and return it"""
        image = None  # will store a copy of the image

        #open dialog for file/open:
        img_file = filedialog.askopenfile(mode='r', filetypes=[
            ('JPEG','*.jpg'),
            ('GIF', '*.gif'),
            ('PNG', '*.png')
        ])

        if img_file != None:  #allows you to hit Cancel without throwing an error
            #save a copy of the image:
            image = Image.open(img_file.name).copy()

        return image

    def setImage(self, img):
        """
        :param img: an image that has been opened (with Image.open())
        :return:none
        """
        self.imageChosen = img

    def getImage(self):
        """
        :return:the objects open image (opened with Image.open())
        """
        return self.imageChosen

    def edge(self, oldImg):
        """
        Finds the edges of items in an image, uses pixels with .load() (faster than getPixel() and setPixel())

        :param oldImg: the image to be changed
        :return: the new, black and white image that has the edges of interior objects drawn
        """
        img = Image.new("RGB", (oldImg.size[0], oldImg.size[1]), "blue")
        black = (0, 0, 0) #the tuple with the RGB value for black
        white = (255, 255, 255) #the tuple with the RGB value for white
        pixels = oldImg.load()
        newPixels = img.load()
        background = pixels[3, 3]
        #
        #loops down through the image
        for i in range(oldImg.size[1]):
            for j in range(oldImg.size[0]):
                pixel = pixels[j,i]
                r,g,b = pixel
                avg = (r + g + b) / 3 #for the threshold of color change
                br, bg, bb = background
                bAvg = (br + bg + bb) / 3 #for the threshold of color change
                if avg < bAvg - 50 or avg > bAvg + 50 and j + 2 < oldImg.size[0] and pixels[j + 2, i] != background:
                    newPixels[j, i] = black
                    background = pixel
                else:
                    newPixels[j, i] = white

        #
        #loops across the image
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                pixel = pixels[i,j]
                r,g,b = pixel
                avg = (r + g + b) / 3#for the threshold of color change
                br, bg, bb = background
                bAvg = (br + bg + bb) / 3#for the threshold of color change
                if avg < bAvg - 50 or avg > bAvg + 50 and i + 2 < oldImg.size[0] and pixels[i + 2, j] != background:
                    newPixels[i, j] = black
                    background = pixel

        return img

    def toGrayscale(self, oldImg):
        """
        Changes the image to black and white. Alternatively, I could have averaged all the pixels at a point (r,g,b = oldImg.load()[x,y] and oldImg.load()[x,y] = (r + g + b) / 3,
        all within two for loops) ,but this way is shorter and faster.
        :param oldImg:
        :return:
        """
        return oldImg.convert('L')

    def toRed(self, oldImg):
        """
        Adds a red hue to the image by converting it to HSV
        :param oldImg: the image to be altered
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/255., g/255., 0)
                h = (h + -90.0/360.0) % 1.0
                s = s ** 1.5
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def toGreen(self, oldImg):
        """
        Adds a green hue to the image by converting it to HSV
        :param oldImg: the image to be altered
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(0, 0, b/255.)
                h = (h + -90.0/360.0) % 1.0
                s = s ** .65
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def toBlue(self, oldImg):
        """
        Adds a blue hue to the image by converting it to HSV
        :param oldImg: the image to be altered
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(b/255., 0, b/255.)
                h = (h + -90.0/360.0) % 1.0
                s = s ** .65
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def changeSaturation(self, oldImg, contrast):
        """
        Changes the saturation of the image by using an HSV image.
        :param oldImg: the image to be altered
        :param contrast: the altered image
        :return:
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
                s = s ** float(contrast)
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def invertColors(self, oldImg):
        """
        inverts the colors of the image by converting it to HLS (I probably could have used HSV instead)
        :param oldImg: the image to be altered
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                t = (r + g + b) / 3
                h,l,s = colorsys.rgb_to_hls(1.0 - r/255., 1.0 - g/255., 1.0 - b/255.)
                r,g,b = colorsys.hls_to_rgb(h, l, s)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def toWhite(self, oldImg):
        """
        Adds a white hue to the image by increasing the saturation
        :param oldImg: the image to be altered
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
                s = s ** 4
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg

    def toFrenchFlag(self, oldImg):
        """
        Adds the hue of the French flag over the image, as inspired by Facebook's recent tool
        :param oldImg: image to be altered
        :return:the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()

        #BLUE
        for i in range(oldImg.size[0] // 3):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(b/255., 0, b/255.)
                h = (h + -90.0/360.0) % 1.0
                s = s ** .65
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))

        #WHITE
        for i in range(oldImg.size[0] // 3, 2 * oldImg.size[0] // 3):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
                s = s ** 4
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))

        #RED
        for i in range( 2 * oldImg.size[0] // 3, oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/255., g/255., 0)
                h = (h + -90.0/360.0) % 1.0
                s = s ** 1.5
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))

        return oldImg

    def toCustomHSV(self, oldImg, newH, newS, newV):
        """
        Allows the user to change the image's hue, saturation and value
        :param oldImg: the image to be altered
        :param newH: the multiple of 255 for hue
        :param newS: the multiple of 255 for saturation, also the power of the saturation
        :param newV: the multiple of 255 for value
        :return: the altered image
        """
        oldImg = oldImg.convert("RGB") #to make sure it isn't in a different type and won't throw an error later
        pixels = oldImg.load()
        for i in range(oldImg.size[0]):
            for j in range(oldImg.size[1]):
                r, g, b = pixels[i,j]
                h,s,v = colorsys.rgb_to_hsv(r/(255* float(newH)), g/(255 * float(newH)), b/(float(newV) * 255))
                s = s ** float(newS)
                r,g,b = colorsys.hsv_to_rgb(h, s, v)
                pixels[i,j] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
        return oldImg