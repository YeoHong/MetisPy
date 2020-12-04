from skimage.color import rgb2gray  


class ColorToGray():
    def __init__(self, qImage):
        print("Color To Gray!")
        img = rgb2gray(qImage)

