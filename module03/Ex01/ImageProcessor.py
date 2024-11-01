from PIL import Image
import numpy as np

class ImageProcessor:
    def load(self, file):
        img = Image.open(file)
        np_data = np.asarray(img)

        return np_data

    def display(self, np_data):
        arr = self.load(np_data)
        img = Image.fromarray(arr, "RGB")
        img.show()

