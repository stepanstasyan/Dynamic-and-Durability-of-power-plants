import math
import sympy

# Исходные данные:
m = 8.81
L = 4.4
l01 = 1.1
l12 = 0.77
l23 = 1.1
d = 46 * 10 ** (-3)
D = 220 * 10 ** (-3)
h = 15 * 10 ** (-3)
po = 8000
E = 2 * 10 ** 11

print('Исходные данные:\n'
      f'm = {m}\nL = {L} м\nl_01 = {l01} м\nl_12 = {l12} м\n'
      f'l_23 = {l23} м\nd = {d} мм\nD = {D} мм\nh = {h} мм\n'
      f'ρ = {po} кг/м^3\nE = {E} Па\n')

Jxx = (math.pi * d ** 4) / 64

delta11 = (l01 ** 2) * ((L - l01) ** 2) / (3 * E * Jxx * L)
delta12 = (l01 ** 2) * ((L - l01) ** 2) / (
        6 * E * Jxx * L) * (2 * (L - l01 - l12) / (L - l01) + (L - l01 - l12) / l01 -
                            ((L - l01 - l12) ** 3) / (l01 * (L - l01) ** 2))
delta13 = (l01 ** 2) * ((L - l01) ** 2) / (
        6 * E * Jxx * L) * (2 * (L - l01 - l12 - l23) / (L - l01) + (L - l01 - l12 - l23) / l01 -
                            ((L - l01 - l12 - l23) ** 3) / (l01 * (L - l01) ** 2))
delta22 = ((l01 + l12) ** 2) * ((L - l01 - l12) ** 2) / (3 * E * Jxx * L)
delta21 = ((l01 + l12) ** 2) * ((L - l01 - l12) ** 2) / (6 * E * Jxx * L) * \
          (2 * l01 / (l01 + l12) + l01 / (L - l01 - l12) - (l01 ** 3) /
           ((l01 + l12) ** 2 * (L - l01 - l12)))
delta23 = ((l01 + l12) ** 2) * ((L - l01 - l12) ** 2) / (6 * E * Jxx * L) * \
          (2 * (L - l01 - l12 - l23) / (L - l01 - l12) + (L - l01 - l12 - l23) / (l01 + l12)
           - (L - l01 - l12 - l23) ** 3 / ((l01 + l12) * (L - l01 - l12) ** 2))
delta33 = (l01 + l12 + l23) ** 2 * ((L - l01 - l12 - l23) ** 2) / (3 * E * Jxx * L)
delta31 = ((l01 + l12 + l23) ** 2) * ((L - l01 - l12 - l23) ** 2) / (6 * E * Jxx * L) * \
          (2 * l01 / (l01 + l12 + l23) + l01 / (L - l01 - l12 - l23) - (l01 ** 3) /
           ((l01 + l12 + l23) ** 2 * (L - l01 - l12 - l23)))
delta32 = ((l01 + l12 + l23) ** 2) * ((L - l01 - l12 - l23) ** 2) / (6 * E * Jxx * L) * \
          (2 * (l01 + l12) / (l01 + l12 + l23) + (l01 + l12) / (L - l01 - l12 - l23) - ((l01 + l12) ** 3) /
           ((l01 + l12 + l23) ** 2 * (L - l01 - l12 - l23)))

print(f'Определение податливостей:\n{delta12} {delta21}\n{delta13} {delta31}\n{delta23} {delta32}')

list_k = []
list_k.append(abs(delta12 - delta21))
list_k.append(abs(delta13 - delta31))
list_k.append(abs(delta23 - delta32))

print('\nПроверка выполнения закона парности:')
for index, k in enumerate(list_k, start=1):
    if k < 10 ** -5:
        print(f'Закон парности для {index} пары выполняется')
    else:
        print(f'Закон парности для {index} пары НЕ ВЫПОЛНЯЕТСЯ!')

p = sympy.symbols('p')
matrix = sympy.Matrix([
    [delta11 * m * p ** 2 - 1, delta12 * m * p ** 2, delta13 * m * p ** 2],
    [delta21 * m * p ** 2, delta22 * m * p ** 2 - 1, delta23 * m * p ** 2],
    [delta31 * m * p ** 2, delta32 * m * p ** 2, delta33 * m * p ** 2 - 1]
])

determinant = matrix.det()

solution = list(sympy.solveset(sympy.Eq(determinant, 0), p))
for p in solution.copy():
    if p < 0:
        solution.remove(p)

p1 = solution[0]
p2 = solution[1]
p3 = solution[2]

p = p1
Y11 = 1
Y21 = sympy.symbols('Y21')
Y31 = sympy.symbols('Y31')
equation1 = sympy.Eq((delta22 * m * p ** 2 - 1) * Y21 + delta21 * m * Y11 * p ** 2 + delta23 * m * Y31 * p ** 2, 0)
equation2 = sympy.Eq((delta33 * m * p ** 2 - 1) * Y31 + delta32 * m * Y21 * p ** 2 + delta31 * m * Y11 * p ** 2, 0)

solution = sympy.solve([equation1, equation2], Y21, Y31)
Y21 = solution[Y21]
Y31 = solution[Y31]
print(f'Y21 = {round(Y21, 4)}; Y31 = {round(Y31, 4)}')

p = p2
Y12 = 1
Y22 = sympy.symbols('Y22')
Y32 = sympy.symbols('Y32')
equation1 = sympy.Eq((delta11 * m * p ** 2 - 1) * Y12 + delta12 * m * Y22 * p ** 2 + delta13 * m * Y32, 0)
equation2 = sympy.Eq((delta33 * m * p ** 2 - 1) * Y32 + delta32 * m * Y22 * p ** 2 + delta31 * m * Y12 * p ** 2, 0)

solution = sympy.solve([equation1, equation2], Y22, Y32)
Y22 = solution[Y22]
Y32 = solution[Y32]
print(f'Y22 = {round(Y22, 4)}; Y32 = {round(Y32, 4)}')

p = p3
Y13 = 1
Y23 = sympy.symbols('Y23')
Y33 = sympy.symbols('Y33')
equation1 = sympy.Eq((delta11 * m * p ** 2 - 1) * Y13 + delta12 * m * Y23 * p ** 2 + delta13 * m * Y33, 0)
equation2 = sympy.Eq((delta33 * m * p ** 2 - 1) * Y33 + delta31 * m * Y13 * p ** 2 + delta32 * m * Y23, 0)

solution = sympy.solve([equation1, equation2], Y23, Y33)
Y23 = solution[Y23]
Y33 = solution[Y33]
print(f'Y23 = {round(Y23, 4)}; Y33 = {round(Y33, 4)}')


# Проверка условия ортогональности
check_uo = math.sqrt(m) * Y11 * (math.sqrt(m) * Y12) + m * Y21 * Y22 + m * (Y31 * Y32)

if check_uo < 0.6:
    print(f'\nУсловие ортогональности: {check_uo} - Выполняется')
else:
    print(f'\nУсловие ортогональности: {check_uo} - НЕ ВЫПОЛНЯЕТСЯ')

input()
