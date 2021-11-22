#a = int(input("Введите число:"))
#if a < 0:
#    print("NEG")
#elif a == 0:
#    print("ZERO")
#else:
#    print("MORE")
import time
a = 0
while a<=23:
    a = a+1
    print(a)
    time.sleep(0.1)
else:
    while a>=1:
        a = a-1
        print(a)
        time.sleep(0.1)