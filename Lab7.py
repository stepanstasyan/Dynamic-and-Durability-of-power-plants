import math
import numpy
import matplotlib.pyplot as plt

# Исходные данные:
l = 1.24
b = 122
delta = 32
h = 36
po = 7800
E = 2 * 10 ** 11
n = 3000
d_l = 3.7
G = 79.3 * 10 ** 9

print('Исходные данные:\n'
      f'l = {l} м\nb = {b} мм\ndelta = {delta} мм\nh = {h} мм\n'
      f'ρ = {po} кг/м^3\nE = {E:.1e} Па\nn = {n} об/мин\nd/l = {d_l}\nG = {G:.1e}\n')

k = (0.162 * b * delta ** 3) / (1 + 1.43 * (delta / b) ** 2 + 2.87 * (h / b) ** 2)
Yp = 0.038 * delta * b ** 3 + 0.04 * b * delta * (delta ** 2 + h ** 2)
print(f'k = {round(k, 0)} мм^4\nYp = {round(Yp, 0)} мм^4\n')

f1kr = 1 / (4 * l) * math.sqrt(G * k / (po * Yp))
f2kr = 3 * f1kr
f3kr = 5 * f1kr

C1n = math.sqrt(2 / po * Yp * l)

n1 = 1
kn1 = (2 * n1 - 1) * math.pi / 2
n2 = 2
kn2 = (2 * n2 - 1) * math.pi / 2
n3 = 3
kn3 = (2 * n3 - 1) * math.pi / 2
print(f'f1kr = {round(f1kr, 2)} Гц\nf2kr = {round(f2kr, 2)} Гц\nf3kr = {round(f3kr, 2)} Гц\n'
      f'C1n = {round(C1n, 2)}\nkn1 = {round(kn1, 2)}\nkn2 = {round(kn2, 2)}\nkn3 = {round(kn3, 2)}')

step = numpy.arange(0, 1, 0.01)
x = l * step
F1 = C1n * numpy.sin(kn1 * x)
F2 = C1n * numpy.sin(kn2 * x)
F3 = C1n * numpy.sin(kn3 * x)

# fig, ax = plt.subplots()
# ax.set_facecolor('#212946')
# fig.set_facecolor('#212946')
# ax.tick_params(color='#CDCDCD', labelcolor='#CDCDCD')
# for spine in ax.spines.values():
#     spine.set_edgecolor('#CDCDCD')
# plt.xlabel('l, м', fontweight='bold', fontstyle='italic', color='#eeebdd')
# plt.ylabel('F, Гц', fontweight='bold', fontstyle='italic', color='#eeebdd')
# plt.grid(color='#2A3459')
# plt.plot(x, F1, "#eeebdd", linewidth=2, label='F1')
# plt.plot(x, F2, "#eeebdd", linewidth=2, label='F2')
# plt.plot(x, F3, "#eeebdd", linewidth=2, label='F3')
# leg = ax.legend()
#
# n_lines = 10
# diff_linewidth = 1.03
# alpha_value = 0.03
# for n in range(1, n_lines + 1):
#     plt.plot(x, F1,
#              linewidth=2 + (diff_linewidth * n),
#              alpha=alpha_value,
#              color='#08F7FE')
#     plt.plot(x, F2,
#              linewidth=2 + (diff_linewidth * n),
#              alpha=alpha_value,
#              color='#ccffbd')
#     plt.plot(x, F3,
#              linewidth=2 + (diff_linewidth * n),
#              alpha=alpha_value,
#              color='#cdc733')
#
# for artist, col in zip(leg.legendHandles, ['#08F7FE','#ccffbd','#cdc733']):
#     artist.set_color(col)
#
# plt.show()

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


plt.plot(x, F1, "#542e71", linewidth=2, label='F1')
plt.plot(x, F2, "#fb3640", linewidth=2, label='F2')
plt.plot(x, F3, "#fdca40", linewidth=2, label='F3')
leg = ax0.legend()

# ax0.set_xlim(0, 9000)
# ax0.set_ylim(0, 1000)

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
plt.savefig('7 Лаб график', dpi=300)
plt.show()

input()
