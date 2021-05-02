import math
import numpy
import matplotlib.pyplot as plt

# Исходные данные:
l = 1.24
b = 122
d = 46 * 10 ** (-3)
D = 220 * 10 ** (-3)
h = 36
po = 7800
E = 2 * 10 ** 11
Betay = 90
delta = 32
k1l = 1.98
k2l = 4.674
k3l = 7.91
d_l = 3.7
n = 3000

print('Исходные данные:\n'
      f'l = {l} м\nd = {d} мм\nb = {b} мм\nD = {D} мм\nh = {h:.1e} мм\n'
      f'ρ = {po} кг/м^3\nE = {E:.1e} Па\nBetay = {Betay}\ndelta = {delta} мм\n'
      f'k1l = {k1l} мм\nk2l = {k2l} мм\nk3l = {k3l} мм\nd/l = {d_l} мм\nn = {n} мм\n')

# Эмпирические формулы

F = 0.69 * b * delta
Ymin = 0.041 * b * delta * (h ** 2 + delta ** 2)

print(f'F = {round(F, 1)} мм^2\nYmin = {round(Ymin, 0)} мм^4\n')

# Собственные частоты

p1 = (k1l ** 2) * (math.sqrt((E * Ymin * 10 ** -6) / (po * F * l ** 4)))
p2 = (k2l ** 2) * (math.sqrt((E * Ymin * 10 ** -6) / (po * F * l ** 4)))
p3 = (k3l ** 2) * (math.sqrt((E * Ymin * 10 ** -6) / (po * F * l ** 4)))

print(f'p1 = {round(p1, 2)} Гц\np2 = {round(p2, 2)} Гц\np3 = {round(p3, 2)} Гц\n')

# Поправка на ужесточение лопатки

n_hertz = n / 60
B = 0.786 * (d_l) + 0.407 - math.cos(math.radians(Betay)) ** 2
p1w = math.sqrt(p1 ** 2 + B * n_hertz ** 2)
p2w = math.sqrt(p2 ** 2 + B * n_hertz ** 2)
p3w = math.sqrt(p3 ** 2 + B * n_hertz ** 2)

print(f'B={round(B, 3)} Гц\np1w = {round(p1w, 2)} Гц\np2w = {round(p1w, 2)}\np3w = {round(p1w, 2)} Гц\n')

# Данные для построения вибрационной диаграммы:

step = numpy.linspace(0, 9000, 19)

p1w_list = []
p2w_list = []
k1 = []
k2 = []
k3 = []
k4 = []
k5 = []
k6 = []

for n in step:
    p1w_list.append(math.sqrt(p1 ** 2 + B * (n / 60) ** 2))
    p2w_list.append(math.sqrt(p2 ** 2 + B * (n / 60) ** 2))
    k1.append(1 * n / 60)
    k2.append(2 * n / 60)
    k3.append(3 * n / 60)
    k4.append(4 * n / 60)
    k5.append(5 * n / 60)
    k6.append(6 * n / 60)


import matplotlib.ticker as ticker

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = "12"
plt.rcParams["text.usetex"] = True
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
plt.rcParams["font.family"] = "serif"

plt.rc('text.latex', preamble=r"""\usepackage[T2A]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage[english, russian]{babel}
    \usepackage{pscyr}
    \usepackage[eulergreek, italic]{mathastext}""")

x_label = r'N_\textit{об/мин}'
y_label = r'p_\textit{Гц}'

fig0, ax0 = plt.subplots(figsize=(6.29921, 8.3/2))

plt.plot(step, p1w_list,  "#04009a", linewidth=2, label='p1w')
plt.plot(step, p2w_list,  "#02475e", linewidth=2, label='p2w')
plt.plot(step, k1, "#6f9eaf", linewidth=2, label='k1')
plt.plot(step, k2,  "#a9294f", linewidth=2, label='k2')
plt.plot(step, k3,  "#c7753d", linewidth=2, label='k3')
plt.plot(step, k4,  "#9f5f80", linewidth=2, label='k4')
plt.plot(step, k5,  "#5b6d5b", linewidth=2, label='k5')
plt.plot(step, k6, "#542e71", linewidth=2, label='k6')
leg = ax0.legend()

ax0.set_xlim(0, 9000)
ax0.set_ylim(0, 1000)

ax0.minorticks_on()
ax0.grid(which='major', color='k', alpha=0.2, linestyle='-')
ax0.grid(which='minor', color='k', alpha=0.1, linestyle='--')

fig0.tight_layout()
fig0.canvas.draw()

labelsx = [item.get_text() for item in ax0.get_xticklabels()]
labelsx[-2] = '$'+x_label+'$'
labelsx[-1] = None
positionsx = ax0.get_xticks()

labelsy = [item.get_text() for item in ax0.get_yticklabels()]
labelsy[-1] = '$'+y_label+'$'
positionsy = ax0.get_yticks()

ax0.xaxis.set_major_locator(ticker.FixedLocator(positionsx))
ax0.xaxis.set_major_formatter(ticker.FixedFormatter(labelsx))
ax0.yaxis.set_major_locator(ticker.FixedLocator(positionsy))
ax0.yaxis.set_major_formatter(ticker.FixedFormatter(labelsy))
#
plt.savefig('6Лаб график', dpi=300)
plt.show()
