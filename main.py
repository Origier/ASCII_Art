from PIL import Image
import sys

ASCII = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
CHARS = len(ASCII)
TERMINAL_WIDTH = 155
TERMINAL_HEIGHT = 80

def getRGBs(image):
    """
    image is an image object from the PIL library

    returns the two dimensional array of RGB's for each pixel in the image
    """
    values = list(image.getdata())
    width, height = image.size
    valuesArray = []
    counter = 0
    for y in range(height):
        tempArray = []
        for x in range(width):
            tempArray.append(values[counter])
            counter += 1
        valuesArray.append(tempArray)
    return valuesArray

def getBrightness(image, processing = 0):
    """
    image is an image object from the PIL library
    processing is the method of calculating the brightness
    0 = Average
    1 = Lightness: ((max(R,G,B) + min(R,G,B)) / 2)
    2 = Luminosity: 0.21R + 0.72G + 0.07B

    returns the two dimensional array of the brightness for pixel in the image
    """
    rgbArray = getRGBs(image)
    if(type(rgbArray[0][0]) == int):
        return rgbArray
    width, height = image.size
    valueArray = []
    for y in range(height):
        tempArray = []
        for x in range(width):
            total = 0
            average = 0
            if(processing == 0):
                for value in rgbArray[y][x]:
                    total += value
                average = round(total /  3)
            elif(processing == 1):
                average = round((max(rgbArray[y][x]) + min(rgbArray[y][x])) / 2)
            elif(processing == 2):
                average = round((0.21 * rgbArray[y][x][0]) + (0.72 * rgbArray[y][x][1]) + (0.07 * rgbArray[y][x][2]))
            else:
                raise ValueError("That isn't a value for processing: try 0 - 2")
            tempArray.append(average)
        valueArray.append(tempArray)
    return valueArray

def imageToASCII(image, processing = 0):
    """
    image is an image object from the PIL Library

    returns an array of ASCII characters that map to the image
    """
    brightness = getBrightness(image, processing)
    valueArray = []
    width, height = image.size
    divisor = 255 / CHARS
    for y in range(height):
        tempArray = []
        for x in range(width):
            asciiValue = round(brightness[y][x] / divisor) - 1
            tempArray.append(ASCII[asciiValue])
        valueArray.append(tempArray)
    return valueArray

def scaleImage(image):
    """
    image is an image object from the PIL Library

    returns an image that fits the size of the terminal
    """
    width, height = image.size
    while(True):
        if(height > TERMINAL_HEIGHT):
            divisor = height / TERMINAL_HEIGHT
            height = round(height / divisor)
            width = round(width / divisor)
        elif(width > TERMINAL_WIDTH):
            divisor = width / TERMINAL_WIDTH
            width = round(width / divisor)
            height = round(height / divisor)
        else:
            break
    return image.resize((width, height))


def main():
    if len(sys.argv) >= 2:
        try:
            im = Image.open(sys.argv[1])
            if(len(sys.argv) > 2):
                processing = int(sys.argv[2])
            else:
                processing = 0
            print("Successfully loaded image!")
            width, height = im.size
            print("Image size: " + str(height) + " x " + str(width))
            im = scaleImage(im)
            width, height = im.size
            print("Scaled size to: " + str(height) + " x " + str(width))
            imageArray = imageToASCII(im, processing)
            print("Successfully constructed ascii matrix!")
            for y in range(height):
                for x in range(width):
                    print(str(imageArray[y][x]) + str(imageArray[y][x]), end = "")
                print("")
        except Exception as ex:
            print(ex)
    else:
        print("Please pass the name of the image as an arguement.")

if __name__ == "__main__":
    main()
