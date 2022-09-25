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
        draw.rectangle(vertice, outline='red', width=5)
    img.save(f'output_yandex/{img_path}')
    
    return img

# def crop_center(img_path, scale):
#     img = Image.open(f'data/{img_path}')

#     img_width, img_height = img.size
#     img_crop = img.crop()
#     img_crop.save(f'buffer/{img_path}')
#     return f'buffer/{img_path}'
