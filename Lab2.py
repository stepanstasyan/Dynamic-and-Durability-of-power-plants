import math
import numpy
import matplotlib.pyplot as plt

# Исходные данные:
l = 1.24
d = 46 * 10 ** (-3)
D = 220 * 10 ** (-3)
h = 29 * 10 ** (-3)
po = 8000
E = 2 * 10 ** 11
P = 1
w = 314
R_l = 2.3

print('Исходные данные:\n'
      f'l = {l} м\nd = {d} мм\nD = {D} мм\nh = {h} мм\n'
      f'ρ = {po} кг/м^3\nE = {E} Па\nR/l = {R_l}\n')

m = po * (math.pi * D ** 2 * h) / 4
Yxx = (math.pi * d ** 4) / 64
delta11 = P * ((2 * l) ** 3) / (48 * E * Yxx)
p = math.sqrt(1 / (delta11 * m))
pw = math.sqrt(p ** 2 + w ** 2 * R_l)

step = numpy.linspace(0, 1, 1000)
x = []
y = []
for i in step:
    x.append(w * i)
    y.append(math.sqrt(p ** 2 + (w * i) ** 2 * R_l))

fig, ax = plt.subplots()
ax.set_facecolor('#f4f4f2')
fig.set_facecolor('#e8e8e8')
ax.patch.set_alpha(0.9)
plt.title('Влияние вращения на частоту собственных колебаний',fontsize = '11', fontweight='bold', fontstyle='normal', color = '#495464')
plt.xlabel('W, рад/с', fontweight='bold', fontstyle='italic', color = '#495464')
plt.ylabel('pw, рад/с', fontweight='bold', fontstyle='italic', color = '#495464')
plt.grid()
plt.plot(x, y, "#495464", linewidth=2)
plt.show()

input()
