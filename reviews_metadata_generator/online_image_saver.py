import requests
import os

from PIL import Image


class OnlineImageSaver:

    def __init__(self, save_directory):
        self._save_directory = save_directory

    def save_image(self, image_url, image_name):
        response = requests.get(image_url, stream=True)
        image = Image.open(response.raw)
        image.save(os.path.join(self._save_directory, f"{image_name}.jpg"))
