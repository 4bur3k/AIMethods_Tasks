from PIL import Image, ImageDraw
import os.path


#Select an area with arguments and save an image
#Rake 2 arguments: 
#verticies - array of arrays of 2 verticies: [[(x, y), (x, y)], ..., [(x, y), (x, y)]],
#image - image file
def select_area(vertices, img_path):
    img = Image.open(f'./data/{img_path}')
    draw = ImageDraw.Draw(img)
    for vertice in vertices:
        draw.rectangle(vertice, outline='red', width=10)
    img.save(f'output_yandex/{img_path}')
    
    return img
