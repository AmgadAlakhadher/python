# Сохранение изображения в текущую папку в формате JPEG:
img.save("tmp.jpg")
# Сохранение изображения в текущую папку в формате BMP:
img.save("tmp.bmp", "BMP")
# Сохранение изображения в текущую папку в формате BMP с использованием файлового объекта:
f = open("tmp2.bmp", "wb")
img.save(f, "BMP")
f.close()