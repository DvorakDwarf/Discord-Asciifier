import cv2
import math

ASPECT_RATIO = 0.493 #Ratio of width to height for font

ASCII_CHARS = ["#", "%", "?", "+", ":", "·", "·"]
ASCII_CHARS_BACKWARDS = ["·", "·", ":", "+", "?", "%", "#"]
ASCII_MONOCHROME = ["#", "·"]

size = 1
ascii_scheme = ASCII_CHARS
path = ''

print("OPTIONS:\nPress enter on any option to choose default")
R1 = input("What size do you want ? \nD - discord-sized message(default), else, type desired size\n")
R2 = input("What type do you want ? \n1 - \"Monochrome\" \n2 - Bigger character = more dark (default) \n3 - Bigger character = more bright\n")
R3 = input("Should max/min brightness be represented as empty space or a · ?\nPress y for · and n for empty space (default)\n")
R4 = input("What is the path to the image ?\n")
R5 = input("What is the path for the .txt file (include name and .txt extension) ?\n")

# R4 = r"Put predetermined image path here"
# R5 = r"Put predetermined .txt path here"

if R1 != "D" and R1 != "":
    size = float(R1)

if R2 == "1":
    ascii_scheme = ASCII_MONOCHROME
elif R2 == "2":
    ascii_scheme = ASCII_CHARS
elif R2 == "3":
    ascii_scheme = ASCII_CHARS_BACKWARDS
    
if R3 != "y":
    new_scheme = []
    for character in ascii_scheme:
        if character == "·":
            new_scheme += " "
        else:
            new_scheme += character
    ascii_scheme = new_scheme
            

if R4 != "":
    path = R4
            
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
ascii = "`\n"
for col in small:
    for row in col:
        ascii += ascii_scheme[int(row // num)];
    ascii += "\n"

ascii += "`"
    
text_file = open(R5, "w")
n = text_file.write(ascii)
text_file.close()
  
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Done")