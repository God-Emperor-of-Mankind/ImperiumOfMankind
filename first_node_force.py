def scalar(a, b):
    return a[0]*b[0]+a[1]*b[1]

def force_approximation(x, u, l, EF):
    N1prime = -1 / l
    N2prime = 1 / l
    N = [N1prime, N2prime]
    return scalar(N, u) * EF

def fnf(u1, u2, EF1):
    print("Усилия для первого элемента")
    print("В 0 - ", force_approximation(0, [u1, u2], 1, EF1))
    print("В 0.25 - ", force_approximation(0.25, [u1, u2], 1, EF1))
    print("В 0.5 - ", force_approximation(0.5, [u1, u2], 1, EF1))
    print("В 0.75 - ", force_approximation(0.75, [u1, u2], 1, EF1))
    print("В 1 - ", force_approximation(1, [u1, u2], 1, EF1))