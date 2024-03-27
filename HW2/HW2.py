def problem_2():
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


def problem_3():
    import math
    p = 21**(1.0/3)
    def a(x):
        return (20*(x**3)+21)/(21*(x**2))
    
    def b(x):
        return x- (x**3 - 21)/(3*(x**2))
    
    def c(x):
        return x - (x**4 - 21*x)/(x**2 - 21)
    
    def d(x):
        return math.sqrt(21/x)

    def Alpha(f, x):
        return math.log(abs((f(x) - p)/(x - p)))
    
    functions = {"a": a, "b": b, "c":c, "d": d}

    for i in functions.keys():
        f = functions[i]
        p_now = 1
        for k in range(20):
            p_now = f(p_now)
            # print(k+1, "err:", abs(p_now - p))
        try:
            alpha = Alpha(f, f(p_now))/Alpha(f, p_now)
            print(i, alpha)
        except:
            print(i, "Cannot compute alpha by this method.")

        print("---")

def problem_4():
    x = 0.3334
    g = lambda x : 2**(-x)
    step = 0
    while abs(x-g(x)) >= 10**(-4):
        x = g(x)
        step += 1
        print("step:", step, ",value:", x)
        
def problem_7():
    def secant_method(f, x_1, x_2):
        return x_1 - (f(x_1)*(x_2 - x_1))/(f(x_2) - f(x_1))

    def false_position(f, a_0, b_0, step):
        a, b = [a_0], [b_0]
        for i in range(step):
            s = b[-1] - f(b[-1])*(a[-1]-b[-1])/(f(a[-1]) - f(b[-1]))
            print(f"step{i+2}:", s)
            if f(a[-1])*s > 0:
                a.append(s)
            elif f(a[-1])*s < 0:
                b.append(s)
            else:
                break

    from math import cos
    p = [-1, 0]
    f = lambda x: -x**3 - cos(x)

    print("Secant method: ")
    for i in range(2, 4):
        r = secant_method(f, p[-2], p[-1])
        p.append(r)
        print(f"p_{i}:", r)

    print("False position: ")
    false_position(f, p[0], p[1], 2)

def problem_8():
    def secant_method(f, x_1, x_2):
        return x_1 - (f(x_1)*(x_2 - x_1))/(f(x_2) - f(x_1))
    
    f = lambda x: 1000*(1-(1+x)**(-360))-135000*x
    x = [0.002, 0.01]
    for _ in range(8):
        p = secant_method(f, x[-1], x[-2])
        print(p, f(p))
        x.append(p)

def problem_10():
    def Aitkens_method(f, x_0, step):
        x = [x_0, f(x_0), f(f(x_0))]
        for i in range(step):
            p = x[-3] - ((x[-2]-x[-3])**2)/(x[-1] - 2*x[-2] + x[-3])
            print(f"p_{i}: {p}")
            x.append(f(x[-1]))

    def Steffensens_method(f, x_0):
        x = [x_0]
        step = 0
        while abs(x[-1]-f(x[-1])) >= 10**(-4):
            p_0 = x[-1]
            p_1 = f(p_0)
            p_2 = f(p_1)
            p = p_0 - ((p_1 - p_0)**2)/(p_2 - 2*p_1 + p_0)
            print(f"i: {step}, p_0: {p_0}, p_1: {p_1}, p_2: {p_2}, p: {p}")
            x.append(p)
            step += 1

    from math import cos, sqrt
    f = lambda x: cos(x)
    x_0 = 0.5
    print("Aitken\'s method: ")
    Aitkens_method(f, x_0, 5)
    print("Steffensen\'s method: ")
    g = lambda x: sqrt(1 + 1/x)
    y_0 = 2
    Steffensens_method(g, y_0)

def problem_11():
    def Newtons_method(f, g, x_0):
        x = [x_0]
        step = 0
        while abs(f(x[-1])) >=  0.00001:
            p = x[-1] - f(x[-1])/g(x[-1])
            print(f"{step} & {x[-1]} & {f(x[-1])} & {g(x[-1])} & {p}\\\\")
            x.append(p)
            step += 1

    f = lambda x : x**3 - 5*x**2 + 8*x -6
    g = lambda x : 3*x**2 - 10*x + 8
    x_0 = 4
    print(f"--- x_0 = {x_0} ---")
    Newtons_method(f, g, x_0)

def problem_11_e():
    import typing
    from cmath import sqrt  

    Num = typing.Union[float, complex]
    Func = typing.Callable[[Num], Num]

    def diff(f: Func, x: list[Num]):
        a, b = x
        return (f(a) - f(b)) / (a - b)

    def mullers_method(f: Func, x: (Num, Num, Num), iterations: int) -> float:
        x_0, x_1, x_2 = x
        for _ in range(iterations):
            delta_1, delta_2 = diff(f, (x_1, x_0)), diff(f, (x_2, x_1))
            d = (delta_2 - delta_1)/(x_2-x_0)
            b = delta_2 + (x_2-x_1)*d
            D = sqrt(b**2 - 4*f(x_2)*d)
            E = max((b-D, b+D), key=abs)
            # Take the higher-magnitude denominator
            x_3 = x_2 - 2 * f(x_2) / E
            # Advance
            x_0, x_1, x_2 = x_1, x_2, x_3
        return x3

    f = lambda x : x**3 - 5*x**2 + 8*x - 6
    m = mullers_method(f, (0, 1, 2), 1)
    print(m)

if __name__ == "__main__":
    problem_11_e()