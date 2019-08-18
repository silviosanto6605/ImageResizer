#pylint:disable=E0602
#!usr/bin/env/python3

try:
    import PIL
    from PIL import Image
    import os

    WannaGoOn = True

    while WannaGoOn == True:

        imageFile = input("Insert the image name ")
        im1 = Image.open(imageFile)

        largh = int(input("Inserisci la larghezza dell'immagine "))
        altezza = int(input("Inserisci l'altezza dell'immagine "))

        im2 = im1.resize((largh,altezza), Image.NEAREST)
        ext = ".jpg"
        Name = input("Salva con nome: ")
        im2.save(Name + ext)
        wanna_go_on = input("Vuoi continuare il ridimensionamento di altre immagini? ")
        if wanna_go_on  == "Si" or "Sì":
            WannaGoOn = True
        elif wanna_go_on == "No":
            WannaGoOn == False
            exit(0)

except MemoryError:
    print("Errore di memoria")
    exit(0)


except FileNotFoundError:
    print('File non trovato...')
    exit(0)

except ImportError:
    os.system("python pip3 install -r requirements.txt")
    print("I am installing the missing packages.")
    exit(0)


except KeyboardInterrupt:
     print("Exit...")
     exit(0)

except OverflowError:
    print("ERRORE DI MEMORIA! Termino...")
    exit(0)