from PIL import Image
import numpy as np

def sobel(image):
    image_array = np.asarray(image)
    x_filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    y_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    width, height = image.size

    sobel = image.copy()
    sobel = np.asarray(image)
    sobel = sobel.copy()

    for i in range(1,height-1):
        for j in range(1,width-1):
            grid = np.array([   [image_array[i-1][j-1], image_array[i-1][j], image_array[i-1][j+1]], 
                                [image_array[i][j-1], image_array[i][j], image_array[i][j+1]], 
                                [image_array[i+1][j-1], image_array[i+1][j], image_array[i+1][j+1]]
                            ])
            gradientX = np.multiply(x_filter, grid)
            gradientY = np.multiply(y_filter, grid)

            gx = gradientX[2][0] + gradientX[2][1] + gradientX[2][2] - gradientX[0][0] + gradientX[0][1] + gradientX[0][2]
            gy = gradientY[0][2] + gradientY[1][2] + gradientY[2][2] - gradientY[0][0] + gradientY[1][0] + gradientY[2][0]

            total = abs(gx + gy)
            if total > 700:
                sobel[i][j] = total
            else:
                sobel[i][j] = 0
            sobel_img = Image.fromarray(sobel, 'L')
    return sobel_img

if __name__ == "__main__":

    with Image.open('flower.jpg') as image:
        image = image.convert('L')

        sobel = sobel(image)
        sobel.save('sobel_out.png')