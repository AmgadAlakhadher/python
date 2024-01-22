from PIL import Image
import io

# Загрузка изображения из файла
img1 = Image.open("img1.jpg")
img1.show()

# Открытие изображения в бинарном режиме
with open("Tulips.jpg", "rb") as f:
    img2 = Image.open(f)
    img2 = img2.convert("L")
    img2.show()

# Загрузка изображения из файла, используя файловый объект
with open("img2.gif", "rb") as f:
    img3 = Image.open(f)
    img3.show()

# Загрузка изображения из строки, используя модуль StringIO
with open("img2.gif", "rb") as f:
    image_data = f.read()
    img4 = Image.open(io.BytesIO(image_data))
    img4.show()