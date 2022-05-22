import cv2
import numpy as np
import random   

def generate_random_sequence(image):
    sequence = np.zeros(image.shape, np.uint8)
    for i in range(0, len(sequence)):
        for j in range(0, len(sequence[0])):
            sequence[i][j] = random.randint(0, 255)
            
    return sequence

def encrypt_decrypt(sequence, image):
    output = np.zeros(image.shape,np.uint8)
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            image[i][j] = sequence[i][j] ^ image[i][j]
        
            
    return image


if __name__ == "__main__":
    image = cv2.imread('lenna_grayscale.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    sequence = generate_random_sequence(image)
    
    cv2.imshow("lenna", image)
    cv2.waitKey(0)
    
    enc_image = encrypt_decrypt(sequence, image)
    
    cv2.imshow("lenna", enc_image)
    cv2.waitKey(0)
    
    dec_image = encrypt_decrypt(sequence, enc_image)
    cv2.imshow("lenna", dec_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    