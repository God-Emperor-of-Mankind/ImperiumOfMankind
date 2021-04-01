# Матрицы жесткости элементов
# Внешняя нумерация - строки; внутренняя - столбцы
#  EF1 -EF1
# -EF1  EF1

def matrix_priemnyi(EF1, EF2):

    K1 = [[EF1, -EF1],
      [-EF1, EF1]]
    K2 = [[EF2, -EF2],
      [-EF2, EF2]]

    print("K1:", K1)
    print("K2:", K2)

    # Матрица жесткости системы
    K = [[K1[0][0], K1[0][1],            0],
        [K1[1][0], K1[1][1] + K2[0][0], K2[0][1]],
        [0,        K2[1][0],            K2[1][1]]]

    return K
