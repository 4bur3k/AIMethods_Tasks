### Here's my tasks from "AI methods" course at NUST MISIS.


##### Made by BPM-19-3 student Kuznetsov Denis.

---

# Task 1

## Задача: 
* Разработать ПО, осуществляющее решение *данной задачи*\* по анализу информации с использованием ИИ-сервисов (Не менее 3-х)
* Сравнить качество решения выбранных ИИ-сервисов

*\*Мною выбраная задача - распознавание людей на изображениях, в том числе нахождение областей, в которых они находятся и определения их количества*

## Запуск:
Для запуска необходимо установить все зависимости и, находясь в текущей директории, написать в терминале:
```bash
streamlit run main.py
```

## Технологии:
* Python + streamlit
* ИИ-сервисы:
        * Yandex Cloud (Yandex Vision)
        * Google cloud platform
        * IBM Watson
        * Microsoft Azure

*В связи с некотрыми обстоятельствами на данный момент не представляется возможным создать платежный аккаунт в иностранных сервисвах, поэтому я сузил задачу до анализа работы одного лишь Yandex Vision, прсредстовм сравнения работы сервисах на изображениях различного качетсва*

Для анализа я собрал небольшой датасет из 10 изображений, снятых при различном освещении и ракурсе. Так же я имею возможность сжать каждое изображение с выбранным качеством(0-99). Для этого я использую параметр quality метода ``` Image.save(fp, quality) ```

Вся работа с Cloud API происходит в yandex_detection.py

Yandex API в качестве ответа на запрос, содержащий изображение, предоставляет Json, сожержащий ключ FaceDetection с координатами вершин прямоугольника, выделяющего лицо:

```json
{
"faceDetection": {
        "faces": [
              {
                "boundingBox": {
                  "vertices": [
                    {
                      "x": "897",
                      "y": "180"
                    },
                    {
                      "x": "897",
                      "y": "358"
                    },
                    {
                      "x": "1074",
                      "y": "358"
                    },
                    {
                      "x": "1074",
                      "y": "180"
                    }]}]}}
```

Очевидно, что для сравнительного анализа такое представление не подойдет. Поэтому мною была сделана простейшая визуализация. С помощью библиотеки **Pillow**, добавляю на изображение красные прямоугольники, вершинами которых являются полученные значения, а по количеству полученых вершин считаю количество лиц. На выходе я получаю массив, содержащий: изображение и количество распознаных лиц на изображении

```python
return [resoult_image, faces_count]
```

Далее, я, используя **Streamlit**,создал простую веб-страницу. В левой части экрана друг на другом располагаются: меню выбора изображения, ползунок выбора качетсва изображения, меню заyрузки собственных изображений. В правой части: выбранное пользователем в оригинальном качестве и оно же сжатое, с указаной потерей качества.

<image src="https://i.imgur.com/jajHS5i.png" alt="Общий вид веб страницы" width=700>

## Анализ

Начнем с рассмотрения датасета(находится в папке "./data"). На каждом изображениии без труда визуально определяетются все лица. В общем в датасете представлены изображения людей в масках, гримме, черно-белые, в плохом качестве, а также большие группы людей


### Одно лицо
Начнем с простейшей задачи. Распознать всего одно лицо.

<image src="https://i.imgur.com/EZuHDnT.png" alt="Простейшая задача" width=700>

С этой задачей Yandex Vision справляется легко, даже при минмальном качестве. Позже я объясню почему.


#### Маски
<image src="https://i.imgur.com/jajHS5i.png" alt="Человек в маске" width=700>

На данном изображении видно, что "Яндекс" распознает лицо в маске как в оригинальном качестве, так и с искажением. Это вызвано тем, лицо на фотографии занимает почти все простаранство и даже такое искажение не изменяет его черты.


<image src="https://i.imgur.com/rLOIWYJ.png" alt="Качество 20%" width=700>
<image src="https://i.imgur.com/2d4KPsL.png" alt="Качество 0%" width=700>

Тут мы можем заметить, как удаленность и количество объектов влияют на работу алгоритма при уменьшении качества. Если, при двадцатипроцентном качестве он еще распознает лицо мужчины на первом плане, то при минимальном - не справляется даже с ним. При этом, даже в оригинальном качетсве сервис не смог распознать лицо женщины вдали


#### Грим
Изображение - фото трех женщин, загримированных для праздника "День мертвых". При этом черты лица никак не изменены, но ближайшая к зрителю развернута в профиль, закрывая лицо второй. Лицо третьей ничем не закрыто. 

<image src="https://i.imgur.com/QZDsLuI.png" alt="День мертвых" width=700>

Даже без искажений Яндекс обнаруживает только одно лицо - третьей девшки. А при качества менее 10% - перестает распознаавть и ее. Разнообразие красок не позволяет алгоритму верно определить черты лица.


#### Черно-белое фото
Слудеющее изображение - кадр из черно-белого фильма "Змеиная нора" 1948 года. 3 Женщины стоят в ряд, лицо каждой отчетливо видно.

<image src="https://i.imgur.com/nXZJ6Q7.png" alt="20% качетсва" width=700>
<image src="https://i.imgur.com/2ydEhYH.png" alt="0% качетсва" width=700>

При снижении качества до двадцати процентов картинка станвоится заметно хуже, но алгоритм видит все лица. А вот при трех процентах лицо женщины слева перестает распознавться. Возможно, это связано с тем, что ее темная кожа сливается с темной одеждой и тенью за ее спиной, в то время как лица двух других женщин конрастируют на фоне одежды и волос. 


#### Лица, частично закрытые другими объектами
Протестируем работу сервиса на кадре из фильма "Бригада". Один из героев придерживает сигарету пальцами, закрывая ладонью часть лица.

<image src="https://i.imgur.com/d7BX12G.png" alt="0% качетсва" width=700>

Здесь повторяется ситуация с ч/б изображением. Из-за высокого контратса лиц на фоне одежды и заднего плана, алгоритм, несмотря на качество оригинальнго изображения и программное его ухудшение, распознает лица героев. Но не справляется с тем, чье личцо заслонено рукой.


### Скопления людей
Далее проверим поведение алгоритма на большом скоплении людей. 
<image src="https://i.imgur.com/7dKhn0z.png" alt="0% качетсва" width=700>

Тут мы видим, что ни одно лицо не было распознано. Обрежем фото и протестируем на нем.

<image src="https://i.imgur.com/vQOVU16.png" alt="0% качетсва" width=700>

Также безрезультатно. Повторим.

<image src="https://i.imgur.com/MzmuBZU.png" alt="0% качетсва" width=700>

Работает! При том распознает даже лицо с закрытыми глазами. Не обращаем внимания на изображение с нулевым качеством, потому что после обрезания качество и так упало в разы, а после обработки она и вовсе превратилось в неразборчивую смесь пикселей. 

Из этого можно сделать вывод, что при достаточном приближении, то есть отбрасывании лишних объектов, алгортим все-таки распознает лицо, которого раньше не видел.

Повторим эксперимент с еще одним изображением

<image src="https://i.imgur.com/EODmxkc.png" alt="0% качетсва" width=700>

Обрежем

<image src="https://i.imgur.com/ORx9jqe.png" alt="0% качетсва" width=700>

5 из 6! Достаточно обрезав, убрав лишние делати и заведомо труднораспознаваемые лица мы добились точности в 80%.

## Итоги

Было бы не корректно считать каие то абсолютные значения на столь малом датасете, к тому же с совершенно непохожими изображениями. Да и такой задачи не стояло. 
Могу лишь отметить, что Yandex Vision в большей мере справился с задачей. Несмотря на то, что он очень неустойчив к различного рода искажениям изображений, а так же к тому, насколько лицо контрастирует с фоном, он смог распознать большинство предоставленных ему лиц.


Список источников:
* Streamlit documentation - https://docs.streamlit.io/
* Yandex vision - https://cloud.yandex.ru/docs/vision/?from=int-console-empty-state
* 

---

## Task 2:
