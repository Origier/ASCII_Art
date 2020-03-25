from PIL import Image
import sys

def getRGBs(image):
    """
    image is an image object from the PIL library

    returns the two dimensional array of RGB's for each x and y coordinate of the image
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



def main():
    if len(sys.argv) == 2:
        try:
            im = Image.open(sys.argv[1])
            print("Successfully loaded image!")
            width, height = im.size
            print("Image size: " + str(height) + " x " + str(width))
            imageArray = getRGBs(im)
            print("Successfully constructed pixel matrix!")
            print("Iterating through pixel contents: ")
            for y in range(height):
                for x in range(width):
                    print(imageArray[y][x], end = "")
                print('\n')
        except Exception as ex:
            print(ex)
    elif len(sys.argv) > 2:
        print("Please only enter one image name")
    else:
        print("Please pass the name of the image as an arguement.")

if __name__ == "__main__":
    main()
