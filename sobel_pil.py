from PIL import Image, ImageFilter

with Image.open('flower.jpg') as image:
    image = image.convert('L')

    sobel = image.filter(ImageFilter.FIND_EDGES)
    sobel.save('pil_sobel_out.png')