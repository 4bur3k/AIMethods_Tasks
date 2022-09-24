import yandex_request


with open('./data/mask.jpg', 'rb') as image:
   yandex_resoult = yandex_request.request(image)