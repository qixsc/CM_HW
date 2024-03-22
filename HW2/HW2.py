import os

a = [1]
b = [4]

def f(x):
    return x**3 + x + 4

while 1:
    mid = (a[-1] + b[-1])/2
    val = f(mid)
    print(mid, val)
    os.system("pause")

    if abs(val) < 0.001:
        break
    elif val > 0:
        b.append(mid)
    else:
        a.append(mid)
