import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def req():
    response = requests.get('https://vk.com/feed/data')
    print(response.status_code)
    print(response.json())


def mat():
    """x = [1, 2, 3]
    y = [4, 5, 6]
    plt.plot(x, y)
    plt.title('Простой график')
    plt.xlabel('Ось Х')
    plt.ylabel("Ось У")"""
    """cat = ['A', 'B', 'C', 'D']
    val = [12, 24, 36, 48]
    plt.bar(cat, val)
    plt.title("Столбчатая диаграмма")
    plt.xlabel("Категории")
    plt.ylabel("Значения")"""
    labels = ['A', 'B', 'C', 'D']
    sizes = [12, 24, 36, 48]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Круговая диаграмма")
    plt.show()



def pil():
    image = Image.open('channels4_profile-4.jpg')
    image_resize = image.resize((300, 450))
    box = (0, 0, 100, 100)
    image_crop = image_resize.crop(box)
    draw = ImageDraw.Draw(image_crop)
    text = "Привет, всем!"
    text = text.encode('utf-8')
    draw.text((10, 0), text, fill='red')
    image_crop.save('channels4_profile-4.jpg')


# pil()
# mat()
req()
