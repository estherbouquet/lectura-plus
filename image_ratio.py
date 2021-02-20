import os.path
from os import path
from PIL import Image

class ImageRatioCalculator:
  def __init__(self, raw_filename):
    print("1 :" + raw_filename)
    self.filename = self.find_existing_img_file(raw_filename)
    self.img_height = None
    self.img_width = None
    self.read_image_dimensions()
    self.aspect_ratio = self.calculate_aspect(self.img_width, self.img_height)

  def find_existing_img_file(self, filename):
    downcase_img_file = "./input/"+filename+".jpg"
    upcase_img_file = "./input/"+filename+".JPG"
    
    if path.exists(downcase_img_file):
      print("File exists:" + downcase_img_file)
      return downcase_img_file
    elif path.exists(upcase_img_file):
      print("File exists:" + upcase_img_file)
      return upcase_img_file
    else:
      return None

  def read_image_dimensions(self):
    if self.filename is not None:
      img = Image.open(self.filename)
      self.img_width, self.img_height = img.size
      return img.size
    else:
      pass

  def calculate_aspect(self, width, height):
    if width is None or height is None:
      return None
    else:      
      def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
      
      r = gcd(width, height)
      x = int(width / r)
      y = int(height / r)

      return x / y

  def horizontal_ratio(self):
    if self.aspect_ratio is None or self.aspect_ratio < 1.01:
      return False
    else:
      self.rotate_image()
      return True
      
  def rotate_image(self):
    image = Image.open(self.filename)
    out = image.rotate(270, expand=True)
    out.save(self.filename)
      
    
