from PIL import Image
import sys

def getRGBs(image):
    """
    image is an image object from the PIL library

    returns the two dimensional array of RGB's for each pixel in the image
    """
    values = list(image.getdata())
    height, width = image.size
    valuesArray = []
    counter = 0
    for y in range(height):
        tempArray = []
        for x in range(width):
            tempArray.append(values[counter])
            counter += 1
        valuesArray.append(tempArray)
    return valuesArray

def getBrightness(image):
    """
    image is an image object from the PIL library

    returns the two dimensional array of the brightness for pixel in the image
    """
    rgbArray = getRGBs(image)
    height, width = image.size
    valueArray = []
    for y in range(height):
        tempArray = []
        for x in range(width):
            total = 0
            average = 0
            for value in rgbArray[y][x]:
                total += value
            average = round(total /  3)
            tempArray.append(average)
        valueArray.append(tempArray)
    return valueArray

def main():
    if len(sys.argv) == 2:
        try:
            im = Image.open(sys.argv[1])
            print("Successfully loaded image!")
            height, width = im.size
            print("Image size: " + str(height) + " x " + str(width))
            imageArray = getRGBs(im)
            print("Successfully constructed pixel matrix!")
            imageArray = getBrightness(im)
            print("Successfully constructed brightness matrix!")
            for y in range(height):
                for x in range(width):
                    print(str(imageArray[y][x]) + " ", end = "")
                print("")
        except Exception as ex:
            print(ex)
    elif len(sys.argv) > 2:
        print("Please only enter one image name")
    else:
        print("Please pass the name of the image as an arguement.")

if __name__ == "__main__":
    main()
