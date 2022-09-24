from PIL import Image, ImageDraw

img = Image.open("data/mask.jpg")  
draw = ImageDraw.Draw(img)
draw.rectangle([(426, 254),(1153, 982)], outline='red') # Рисуем красную точку по координатам 10x10
img.show()
