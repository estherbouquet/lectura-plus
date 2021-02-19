import os.path
from os import path
from PIL import Image

class ImageRatioCalculator:
  def __init__(self, raw_filename):
    self.filename = self.find_existing_img_file(raw_filename)
    self.img_width = None
    self.img_height = None
    self.read_image_dimensions()
    self.aspect_ratio = self.calculate_aspect(self.img_width, self.img_height)

  def find_existing_img_file(self, filename):
    downcase_img_file = f"{filename}.jpg"
    upcase_img_file = f"{filename}.JPG"

    if path.exists(downcase_img_file):
      return downcase_img_file
    elif path.exists(upcase_img_file):
      return upcase_img_file
    else:
      return None

  def read_image_dimensions(self):
    if self.filename:
      img = Image.open(self.filename)
      self.img_width, self.img_height = img.size
      return img.size
    else:
      pass

  def calculate_aspect(self, width, height):
    def gcd(a, b):
      return a if b == 0 else gcd(b, a % b)

    r = gcd(width, height)
    x = int(width / r)
    y = int(height / r)

    return x / y

  def horizontal_ratio(self):
    return True if self.aspect_ratio > 1.01 else False
