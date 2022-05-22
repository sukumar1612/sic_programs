import numpy as np
import cv2

MAX_ITER = 100

def julia(z, c):
    n = 0
    while np.abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def drawImage(c):
    img_width = 600
    img_height = 400
    
    ranger = [-2, 2]
    rangei = [2, -2]
    
    
    image = [[[0,0,0] for i in range(img_width)] for j in range(img_height)]
    
    for y in range(img_height):
        for x in range(img_width):        
            zr = ranger[0] + (float(x)/float(img_width))*(ranger[1] - ranger[0]) 
            zi = rangei[0] + (float(y)/float(img_height))*(rangei[1] - rangei[0])
            z = complex(zr, zi)
            
            n = julia(z, c)
            color_r = 255 - (n * 255 / MAX_ITER) % 255
            color_g = 255 - (n * 255 / MAX_ITER) % 255
            color_b = 255 - (n * 255 / MAX_ITER) % 255
            
            if n==MAX_ITER:
                color_r = 0
                color_g = 0
                color_b = 0

            
            image[y][x] = [color_r, color_g, color_b]
    
    image = np.array(image, np.uint8)
    image = cv2.cvtColor(image, cv2.IMREAD_COLOR)

    cv2.imshow("mandelbrot", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    drawImage( 0.285+0.01j)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        