#!/usr/bin/python3
import sys
 
#pour le traitement des images
from PIL import Image, ImageOps
import numpy as np
import argparse
 
def getImageFromFileSystemAndConvertToBlackAndWhite(pathToImage):
    myImage = Image.open(pathToImage)
    myImage = myImage.rotate(180) #rotate image
    myImage = myImage.convert('L') #grayscale
    myImage = ImageOps.invert(myImage) #invert grayscale
    myImage = myImage.convert('1') #turn into b&w pix
    myImage.save('converted'+pathToImage) #save as converted+nameoftheimage
    return myImage
   
#convert an image to a 2D array representing each pixel as True (White) and False(Black)
def imageToArray(image):
    return np.asarray(image)
 
def PixelsToOctetToHex(imageAsArray):
    tableauDOctectEnHex = []
    #on crée un paquet de 8 pixels en passant par tous les 8 pixels horizontaux de toute la hauteur de l'image
    for i in range (len(imageAsArray)): #height
        for j in range (0, len(imageAsArray[0]), 8): #width de la ligne 0 ; choix arbitraire
            paquetHuitPixels = imageAsArray[i][j:j+8] #on vient stocker les paquets de 8 pixels obtenus dans une variable
            #on prend notre paquet pour le transformer en octet via la fonction eightbittobyte
            notreOctect = eightBitToByte(paquetHuitPixels)
            #on prend notre octet (composé de notre paquet de 8 pixels) pour le transformer en hexadécimal
            notreOctectEnHex = bytes(notreOctect).hex()
            tableauDOctectEnHex.append(notreOctectEnHex) #on ajoute cet octet en hex à un tableau qui regroupe tous les oct en hex
            #pour faire d'une pierre trois coups :
            #tableauDOctectEnHex.append(bytes(eightBitToByte(paquetHuitPixels)).hex())
    return tableauDOctectEnHex
#convert an array of eight bits to a byte
def eightBitToByte(bitsArray):
    byte = np.packbits(bitsArray)
    return byte
 
#Format a byte array to a python variable
def byteArrayToImgPy(byteArray, tmpfile):
    for i in range(len(byteArray)):
        byteArray[i] = "b'\\x"+(byteArray[i].upper())+"'"
    contenuImageEnHex = ",".join(byteArray)
    contenuImageEnHex = "img = [" + contenuImageEnHex + "]"
    #print(contenuImageEnHex)
    #create a new file to stock the formated array from contenuImageEnHex
    newfile = open(tmpfile, "w+")
    newfile.write(contenuImageEnHex)
    newfile.close()
 
def main(pathToImage, tmpfile):
    imageConvertie = getImageFromFileSystemAndConvertToBlackAndWhite(pathToImage)
    imageAsArray = imageToArray(imageConvertie) #on transforme notre objet image en tableau
    byteArrayToImgPy(PixelsToOctetToHex(imageAsArray), tmpfile)

main(sys.argv[1], sys.argv[2])

