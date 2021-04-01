def scalar(a, b):
    return a[0]*b[0]+a[1]*b[1]

def approximation(x, u, l):
    N1 = 1 - x / l
    N2 = x / l
    N = [N1, N2]
    return scalar(N, u)

def fnd(u1, u2):
    print("Перемещения для первого элемента")
    print("В 0 - ", approximation(0, [u1, u2], 1))
    print("В 0.25 - ", approximation(0.25, [u1, u2], 1))
    print("В 0.5 - ", approximation(0.5, [u1, u2], 1))
    print("В 0.75 - ", approximation(0.75, [u1, u2], 1))
    print("В 1 - ", approximation(1, [u1, u2], 1))