import yandex_detection
import google_detection

yandex_resoult = yandex_detection.detect_faces('me_1.jpg')
print(yandex_resoult[1])

