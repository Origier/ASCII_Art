from PIL import Image
import sys

def main():
    if len(sys.argv) == 2:
        im = Image.open(sys.argv[1])
        print("Successfully loaded image!")
        width, height = im.size
        print("Image size: " + str(height) + " x " + str(width))
    elif len(sys.argv) > 2:
        print("Please only enter one image name")
    else:
        print("Please pass the name of the image as an arguement.")

if __name__ == "__main__":
    main()
