from PIL import Image

im = Image.open("stock_photo.jpg")
print(im.format, im.size, im.mode)
