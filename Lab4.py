import math
import sympy


m = 9.0
L = 4.3
l01 = 1.2
l12 = 0.8
l23 = 1.2
d = 49 * 10 ** (-3)
D = 210 * 10 ** (-3)
h = 17 * 10 ** (-3)
po = 8000
E = 2 * 10 ** 11
G = 79.3 * 10 ** 9  # Модуль сдвига
tetad = m * D ** 2 / 16

print('Исходные данные:\n'
      f'm = {m} кг\nL = {L} м\nl_01 = {l01} м\nl_12 = {l12} м\n'
      f'l_23 = {l23} м\nd = {d} мм\nD = {D} мм\nh = {h} мм\n'
      f'ρ = {po} кг/м^3\nE = {E} Па\nθd = {round(tetad, 3)}\n')

print(f'Модуль сдвига:\nG = {G:1.3e} Па\n')
# Полярный момент иннерции вала
lp = (math.pi * d ** 4) / 32
print(f'Полярный момент инерции вала:\nlp = {lp:1.3e} м^4\n')

# Жесткость вала
c12 = G * lp / l12
c23 = G * lp / l23
print(f'Жесткость вала:\nc12 = {round(c12, 2)} Н/м\nc23 = {round(c23, 2)} Н/м\n')

Fi1 = 1
Fi2 = sympy.symbols('Fi2')
Fi3 = sympy.symbols('Fi3')
p = sympy.symbols('p')

equation1 = sympy.Eq(0 - p ** 2 * tetad * Fi1 + c12 * (Fi1 - Fi2), 0)
equation2 = sympy.Eq(-c12 * (Fi1 - Fi2) - p ** 2 * tetad * Fi2 + c23 * (Fi2 - Fi3), 0)
equation3 = sympy.Eq(-c23 * (Fi2 - Fi3) - p ** 2 * tetad * Fi3, 0)

solution = sympy.solve([equation1, equation2, equation3], p, Fi2, Fi3, dict=True)

solution_list = [sol[p] for sol in solution if sol[p] > 0]
print(
    f'Частоты крутильных колебаний:\nP1n = {round(solution_list[0], 2)} рад/c\nP2n = {round(solution_list[1], 2)} рад/c'
)

input()
