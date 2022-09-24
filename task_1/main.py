import yandex_request


yandex_resoult = yandex_request.request('face-detection-sample.jpg')
print(yandex_resoult[1])