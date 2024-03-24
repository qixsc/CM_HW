a = [1]
b = [4]

def f(x):
    return x**3 + x - 4

while 1:
    mid = (a[-1] + b[-1])/2
    val = f(mid)
    print(mid, val)

    if abs(val) < 0.0001:
        break
    elif val > 0:
        b.append(mid)
    else:
        a.append(mid)
