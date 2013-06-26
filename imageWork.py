#!/usr/bin/python
from randomizer import randomizer 
from databaseActions import imageCount, fetchURL
def pickRandomImageName():
   
    imageIdArray = imageCount()
    lengthOfArray = len(imageIdArray)
    randomNumber = randomizer(lengthOfArray)
    name = fetchURL(imageIdArray[randomNumber])
    return name
