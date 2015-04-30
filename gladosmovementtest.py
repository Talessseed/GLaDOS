import pygame.camera
import pygame.image
from numpy import *

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
imagepix =  array([ [],[] ])
imagepix= imagepix.reshape("720x1280")

def capture():
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, "photo.bmp")
    pygame.camera.quit()

def image_to_matrice():
    im = Image.open('image.gif')
    rgb_im = im.convert('RGB')
    
for x in range(0,1279):
    for y in range(0,719):
        ligne=[]
        r, g, b = rgb_im.getpixel((x, y))
        terrain[x,y]=[r,g,b]
    
