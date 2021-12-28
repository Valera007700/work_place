

#class Point:
#    color = "red"
#    circle = 23

#print(Point.color, Point.circle)
#class Point:
#    color = "green"
#print(Point.color)

#a = 17
#b = True if a > 10 else False
#print(b, Point.color)


a = 2
while a<5:
    print(a, "Это до")
    a = a+1
    print(a, "----Это после")
else:
    print("NCE")

#___________
awdawd


class Pount:
    "Класс для представления координат на полокости "
    color = "red"
    circle = 2

##<><><><><><>
Point.color = "black" - меняем атрибут в классе 
Point.__dict__ - пказывает все атрибуты в классе Point
getattr(point, "color", False)
Point.__doc__ - То, что написано в комментакх после определения класса. 
