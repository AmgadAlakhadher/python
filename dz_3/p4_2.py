from PIL import Image

# Открытие изображения
img = Image.open("img.jpg")

# Преобразование изображения в режим RGBA
img_rgba = img.convert("RGBA")

# Просмотр изображения
img_rgba.show()