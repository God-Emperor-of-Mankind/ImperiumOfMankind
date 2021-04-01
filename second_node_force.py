def scalar(a, b):
    return a[0]*b[0]+a[1]*b[1]

def force_approximation(x, u, l, EF):
    N1prime = -1 / l
    N2prime = 1 / l
    N = [N1prime, N2prime]
    return scalar(N, u) * EF

def snf(u2, u3, EF2):
    print("Усилия для второго элемента")
    print("В 0 - ", force_approximation(0, [u2, u3], 1, EF2))
    print("В 0.25 - ", force_approximation(0.25, [u2, u3], 1, EF2))
    print("В 0.5 - ", force_approximation(0.5, [u2, u3], 1, EF2))
    print("В 0.75 - ", force_approximation(0.75, [u2, u3], 1, EF2))
    print("В 1 - ", force_approximation(1, [u2, u3], 1, EF2))