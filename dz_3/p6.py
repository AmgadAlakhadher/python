from PIL import Image

# Создание черного квадрата
img = Image.new("RGB", (100, 100))
img.show()

# Создание красного квадрата
img = Image.new("RGB", (100, 100), (255, 0, 0))
img.show()

# Создание зеленого квадрата
img = Image.new("RGB", (100, 100), "green")
img.show()

# Создание красного квадрата
img = Image.new("RGB", (100, 100), "#f00")
img.show()

# Создание белого квадрата
img = Image.new("RGB", (100, 100), "white")
img.show()

# Создание серого квадрата
img = Image.new("RGB", (320, 240), "silver")
img.show()

# Создание цветного прямоугольника
img = Image.new("RGB", (320, 240), "rgb(205, 100,200)")
img.show()

# Создание цветного прямоугольника (Каналы в процентах)
img = Image.new("RGB", (320, 240), "rgb(10%, 100%,40%)")
img.show()

# Создание цветного прямоугольника заданного цвета и изменение цвета
img = Image.new("RGB", (640, 480), "rgb(205, 100,200)")
img.show()
for x in range(640):
    for y in range(480):
        img.putpixel((x,y),(0,160,0))
img.save("okno.png", "PNG")
img.show()

# Создание прямоугольника заданного цвета с функциональной раскраской
img = Image.new("RGB", (640, 480), "rgb(205, 100,200)")
img.show()
for x in range(640):
    for y in range(480):
        img.putpixel((x,y), (x//3, (x+y)//6, y//3))
img.save("okno.png", "PNG")
img.show()
