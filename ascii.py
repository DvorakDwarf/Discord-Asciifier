import cv2
import math

ASPECT_RATIO = 0.493 #Ratio of width to height for font
  
ASCII_CHARS = ["#", "%", "?", "+", ":", "·", "·"]
ASCII_CHARS_BACKWARDS = ["·", "·", ":", "+", "?", "%", "#"]
ASCII_MONOCHROME = ["#", "·", "·"]

def image_to_text(path, palette = ASCII_CHARS, background = 'n', size = 1):
  if palette == "d":
      palette = ASCII_CHARS
  elif background == "d":
      background = 'n'
  elif size == "d":
      size = 1
  
  ascii_scheme = palette

  R2 = palette
  
  if R2 == "1":
      ascii_scheme = ASCII_MONOCHROME
  elif R2 == "2":
      ascii_scheme = ASCII_CHARS
  elif R2 == "3":
      ascii_scheme = ASCII_CHARS_BACKWARDS
      

  R3 = background  
  if R3 == "y":
      new_scheme = []
      for character in ascii_scheme:
          if character == "·":
              new_scheme += " "
          else:
              new_scheme += character
      ascii_scheme = new_scheme
              
  
  # if R4 != "":
  #     path = R4
              
  print("\nCreating image")
  
  #Open up image, turn greyscale, resize
  image = cv2.imread(path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  width, height = gray.shape
  height *= 0.493
  image_ratio = width * height
  x = 1920 / image_ratio
  x = math.sqrt(x)
  
  width_ratio = x * size
  height_ratio = x * 0.493 * size
  
  small = cv2.resize(gray, (0, 0), fx=width_ratio, fy=height_ratio)
  
  num = 255/(len(ascii_scheme)-1.01)
  
  print(ascii_scheme)
  
  ascii = "`\n"
  for col in small:
      for row in col:
          ascii += ascii_scheme[int(row // num)];
      ascii += "\n"
  
  ascii += "`"
  
  print("Done")
  
  if size != 1:
        text_path = r'E:\Code\Code_projects\Bapple\testtext.txt'
        text_file = open(text_path, "w")
        text_file.write(ascii)
        text_file.close()
        return text_path
    
  return ascii