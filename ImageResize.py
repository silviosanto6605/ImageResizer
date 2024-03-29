# !usr/bin/env/python3


__author__ = "Silvio Santoriello"
import os
import sys
import platform
try:
    import PIL
    from PIL import Image
    from pyfiglet import Figlet

    f = Figlet(font='standard')
    print(f.renderText('ImagerResizer'))
    print("ImageResizer 1.0 by Silvio Santoriello\n",platform.uname())

    imageFile = input("Insert the image name ")
    im1 = Image.open(imageFile)
    number_of_same_images = 1
    incr = 0
    RecursionImage = False
    Recursionverify = input("Vuoi creare più copie della stessa immagine? 1)Sì  2) No  ")
    if Recursionverify == "1":
        RecursionImage = True
        largh = int(input("Inserisci la larghezza dell'immagine "))
        altezza = int(input("Inserisci l'altezza dell'immagine "))

        im2 = im1.resize((largh, altezza), Image.NEAREST)
        number_of_same_images = int(input("MultiFileBaking: Quante altre copie vuoi salvare della suddetta immagine? "))
        ext = ".jpg"
        Name = input("Salva con nome: ")
        while incr != number_of_same_images:
            incr = incr + 1
            incrstr = str(incr)
            im2.save(Name + incrstr + ext)

    elif Recursionverify == "2":
        largh = int(input("Inserisci la larghezza dell'immagine "))
        altezza = int(input("Inserisci l'altezza dell'immagine "))

        im2 = im1.resize((largh, altezza), Image.NEAREST)
        ext = ".jpg"
        Name = input("Salva con nome: ")
        im2.save(Name + ext)


except MemoryError:
    print("Errore di memoria")
    sys.exit()


except FileNotFoundError:
    print('File non trovato...')
    sys.exit()

except ImportError:
    os.system("pip3 install -r requirements.txt")
    print("I am installing the missing packages.")
    sys.exit()


except KeyboardInterrupt:
    print("Exit...")
    sys.exit()

except OverflowError:
    print("ERRORE DI MEMORIA! Termino...")
    sys.exit()

except FileExistsError:
    print("Uno o più file possiedono un nome che coincide con un altro file esistente sull'hard drive. Cambia nome o elimina i file che sono in conflitto")

except OSError:
    print("Se visualizzi l'errore, hai fatto una di queste cose:\nL'immagine ridimensionata supera il limite di 65500 pixel.\n Hai selezionato un file non valido, corrotto o non riconosciuto. Usa ImageConvert.py per convertire l'immagine oppure seleziona un file valido")
    print("ATTENZIONE: Il file ora generato è corrotto.")
