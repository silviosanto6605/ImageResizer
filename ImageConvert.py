# !usr/bin/env/python3


__author__ = "Silvio Santoriello"
import os
import sys
import platform
try:
    from PIL import Image
    from pyfiglet import Figlet

    f = Figlet(font='standard')
    print(f.renderText('ImageConverter'))
    print("ImageConverter 1.0 by Silvio Santoriello\n",platform.uname())

    path = input("Insert image name ")
    im = Image.open(path)
    name = input("Save as: ")
    im.convert('RGB').save(name+".jpg","JPEG")
    print("Now you can use the file just created with ImageResizer")

except MemoryError:
    print("Memory error :(")
    os.exit(0)


except ImportError:
    os.system("pip3 install --user -r requirements.txt")
    print("I am installing the missing packages.")
    os.exit()
