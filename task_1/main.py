import yandex_request


yandex_resoult = yandex_request.request('masks.jpg')
print(yandex_resoult[1])