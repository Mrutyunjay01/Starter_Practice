import cv2


class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter


    def preprocess(self, image):
        """
        resize the image to a fixed size ignoring the aspect ratio.
        :param image:
        :return: processed image
        """
        return cv2.resize(image, (self.width, self.height),
                          interpolation=self.inter)