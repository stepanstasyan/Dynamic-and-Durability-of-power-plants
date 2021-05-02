import math
import numpy
import sympy


l = 1.24
d = 46 * 10 ** (-3)
D = 220 * 10 ** (-3)
h = 29 * 10 ** (-3)
po = 8000
E = 2 * 10 ** 11
P = 1
print('Исходные данные:\n'
      f'l = {l} м\nd = {d} мм\nD = {D} мм\nh = {h} мм\n'
      f'ρ = {po} кг/м^3\nE = {E} Па\nP = {P}\n')

# Определение собственной частоты поперечных
# колебаний ротора с диском,
# расположенным между опорами

m = po * ((math.pi * D ** 2) / 4) * h
Yxx = (math.pi * d ** 4) / 64
delta11 = (P * (2 * l) ** 3) / (48 * E * Yxx)
p_opor = math.sqrt(1 / (delta11 * m))
p_opor_hertz = p_opor / (2 * math.pi)

print(f'Собственная частота поперечных колебаний ротора с диском,\n'
      f'расположенным между опорами: {round(p_opor_hertz, 2)} Гц')

# Определение собственной частоты поперечных колебаний для:
# Консольного расположения диска

m = m
Yx0 = (math.pi * d ** 4) / 64
delta11 = l ** 3 / (3 * E * Yx0)
p_consol = math.sqrt(1 / (delta11 * m))
p_consol_hertz = p_consol / (2 * math.pi)

print(f'Собственная частота поперечных колебаний ротора с консольно\n'
      f'расположенным диском без учета момента иннерции: {round(p_consol_hertz, 2)} Гц')

# С учетом момента инерции диска

delta11 = delta11
delta21 = l ** 2 / (2 * E * Yx0)
delta12 = delta21
delta22 = l / (E * Yx0)

teta_x = (m * (0.5 * D) ** 2) / 2

p = sympy.symbols('p')
solution = sympy.solve(
    sympy.Eq(
        p ** 4 * m * teta_x * (delta11 * delta22 - delta12 * delta21) - p ** 2 * (teta_x * delta22 + delta11 * m) + 1,
        0),
    p)
for i in solution.copy():
    if i < 0:
        solution.remove(i)
p1 = solution[0]
p2 = solution[1]
print(
    f'С учетом момента иннерции: Pmin = {round(p1 / (2 * math.pi), 2)} Гц; Pmax = {round(p2 / (2 * math.pi), 2)} Гц')

#  Проверка ортогональности

Y1 = 1
Y2 = 1

F1 = (1 - m * (p2 ** 2) * delta11) / (teta_x * (p2 ** 2) * delta12)
F2 = (teta_x * (p1 ** 2) * delta21) / (1 - m * (p1 ** 2) * delta22)
check_uo = Y1 * Y2 * m + teta_x * F1 * F2

print(f'Проверка ортогональности:\nФ1 = {round(F1, 3)}\nФ2 = {round(F2, 3)}\n'
      f'Проверка условия ортогональности: {round(check_uo, 5)}')

# Определение собственных частот крутильных колебаний

m = m
Yx0 = (math.pi * d ** 4) / 64
delta = l / (E * Yx0)
p = math.sqrt(1 / (delta * m))
print(f'Собственная частота крутильных колебаний: {round(p / (2 * math.pi), 2)} Гц')

# Определение характеристик затухания

Ai = 12
Ai1 = Ai - 1
eta = numpy.log(Ai / Ai1)
beta = eta / math.pi

print(f'Характеристики затухания: η = {round(eta, 4)}; β = {round(beta, 4)}')

# change = [
#     ['l', l],
#     ['d', d],
#     ['D', D],
#     ['h', h],
#     [r'\rho', po],
#     ['E', E],
#     ['m', round(m, 5)],
#     [r'Y_{\textit{xx}}', Yxx],
#     ['\delta_{11}', delta11],
#     ['p', p_opor_hertz],
#     ['Yx0', Yx0],
#     ['\delta_{12}', delta12],
#     ['\delta_{21}', delta21],
#     ['\delta_{22}', delta22],
#     [r'\theta_{x}', teta_x],
#     ['p1', p1],
#     ['p2', p2],
#     ['Ф_{1}', F1 ],
#     ['Ф_{2}', F2 ],
#     ['delta', delta],
#     ['\eta', eta],
#     [r'\beta', beta]
# ]
#
# file_dlya_zapisi = codecs.open('отчет1.tex', 'w', encoding='utf8')
# file_s_shablonom = codecs.open('задача1.tex', 'r', encoding='utf8')
# lines = file_s_shablonom.readlines()
# for line in lines:
#     for perem in change:
#         line = line.replace('!!!' + perem[0] + '!!!', str(perem[1]))
#     file_dlya_zapisi.write(line)
# file_dlya_zapisi.close()
# file_s_shablonom.close()

input()