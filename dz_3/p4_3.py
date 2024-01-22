from PIL import Image

# Открытие изображения
img = Image.open("img.jpg")

# Преобразование изображения в формат P с указанием параметров смешивания цветов и адаптивной палитры в 128 цветов
img_p = img.convert("P", palette=Image.ADAPTIVE, colors=128)

# Просмотр изображения
img_p.show()