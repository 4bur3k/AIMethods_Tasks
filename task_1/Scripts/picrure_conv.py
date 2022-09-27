from PIL import Image, ImageDraw
import os.path


#Select an area with arguments and save an image
#Take 2 arguments: 
#verticies - array of arrays of 2 verticies: [[(x, y), (x, y)], ..., [(x, y), (x, y)]],
#image_name - image file name
#service_name - name of service(yandex, google, faceplus)
def select_area(vertices, img_name, service_name):
    img = Image.open(f'../output_{service_name}/{img_name}')

    draw = ImageDraw.Draw(img)

    for vertice in vertices:
        draw.rectangle(vertice, outline='red', width=5)

    img.save(f'../output_{service_name}/{img_name}')
    
    return img

def image_distortion(img_name, quality, service_name):
    img = Image.open(f'../data/{img_name}')
    print(quality)
    img.save(f'../output_{service_name}/{img_name}', quality=quality)
