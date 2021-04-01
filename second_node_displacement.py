def scalar(a, b):
    return a[0]*b[0]+a[1]*b[1]

def approximation(x, u, l):
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    return scalar(N, u)

def snd(u2, u3):
    print("Перемещения для второго элемента")
    print("В 0 - ", approximation(0, [u2, u3], 1))
    print("В 0.25 - ", approximation(0.25, [u2, u3], 1))
    print("В 0.5 - ", approximation(0.5, [u2, u3], 1))
    print("В 0.75 - ", approximation(0.75, [u2, u3], 1))
    print("В 1 - ", approximation(1, [u2, u3], 1))