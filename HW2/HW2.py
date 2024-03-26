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

def problem_7():
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

if __name__ == "__main__":
    problem_7()