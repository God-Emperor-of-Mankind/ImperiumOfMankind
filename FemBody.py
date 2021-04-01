# K - матрица жесткости системы, размерность 3x3
# q - вектор-столбец неизвестных узловых перемещений
# f - вектор-столбец известных внешних нагрузок

# вызываем скрипт ввода начальных данных

from FemInput import get_input
EF1, EF2, F = get_input()

# Матрицы жесткости элементов

from stifness_matrix import matrix_priemnyi
K = matrix_priemnyi(EF1, EF2)
print("Матрица жескости до введения ГУ" + "\n" + "K:", K)

from border_conditions import get_input


print("Матрица жескости после введения ГУ" + "\n" + "K:", K)

# Вектор внешних узловых усилий:
f = [0, F, 0]

print("f:", f)

# Неизвестное перемещение во втором узле:
# u2
u1 = 0
u2 = f[1] / K[1][1]
u3 = 0

u = [u1, u2, u3]

print("u:", u)


