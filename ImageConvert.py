# !usr/bin/env/python3


__author__ = "Silvio Santoriello"
import os
import sys

try:
    import PIL
    from PIL import Image
    import pyfiglet
    from pyfiglet import Figlet
    import platform

    f = Figlet(font='standard')
    print(f.renderText('ImageConverter'))
    print("ImageConverter 1.0 by Silvio Santoriello\n",os.uname())

    path = input("Insert image name ")
    im = Image.open(path)
    name = input("Save as: ")
    im.convert('RGB').save(name+".jpg","JPEG")
    print("Now you can use the file just created with ImageResizer")

except MemoryError:
    print("Memory error :(")
    os.exit(0)


except ImportError:
    os.system("pip3 install -r requirements.txt")
    print("I am installing the missing packages.")
    sys.exit()