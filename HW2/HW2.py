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
    
    functions = {"a": a, "b": b, "c":c, "d": d}

    for i in functions.keys():
        f = functions[i]
        p_now = 1
        for _ in range(10):
            p_now = f(p_now)
            # print(p_now - p)
        
        alpha = math.log(abs((f(f(p_now)) - p)/(f(p_now) - p)))/math.log(abs((f(p_now) - p)/(p_now - p)))
        print(i, alpha)


if __name__ == "__main__":
    problem_3()