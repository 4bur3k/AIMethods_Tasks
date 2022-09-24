from request import yandex_request

with open('./data/mask.jpg', 'rb') as image:
    yandex_request(image)