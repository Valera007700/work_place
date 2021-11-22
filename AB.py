import time
a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b
    time.sleep(1);

