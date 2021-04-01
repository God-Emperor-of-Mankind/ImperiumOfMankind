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

# Применяем ГУ к матрице

from border_conditions import border_condition
K = border_condition(K)
print("Матрица жескости после введения ГУ" + "\n" + "K:", K)

# Вектор внешних узловых усилий:
f = [0, F, 0]

print("Вектор внешних узловых усилий:" + "\n" + "f:", f)

# Неизвестное перемещение во втром узле

from unkown_second_node_displacement import usnd
u = usnd(f, K)
print("Неизвестное перемещение во втром узле:" + "\n" + "u:", u)

