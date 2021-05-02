import codecs
from math import pi, sqrt

# Длина чего-то важного, м
l = 1.24
d = 46*10**-3
D = 220*10**-3
h = 29*10**-3
rho = 8000
E = 2 * 10**11

m = rho * pi * D**2 / 4 * h

Y_xx = pi * d**4/64

P = 1
delta_11 = P * (
        2 * l) ** 3 / (
        48 * E * Y_xx)

p = sqrt(1 / (delta_11 * m))


# ЗДЕСЬ НАЧИНАЕТСЯ ОФОРМЛЕНИЕ
change = [
    ['l', l],
    ['d', d],
    ['D', D],
    ['h', h],
    [r'\rho', po],
    ['E', E],
    ['m', round(m, 5)],
    [r'Y_{\textit{xx}}', Yxx],
    ['\delta_{11}', delta11],
    ['p', p_opor_hertz],
    ['Y_{x0}', Yx0]

]

file_dlya_zapisi = codecs.open('otchet1.tex', 'w', encoding='utf8')
file_s_shablonom = codecs.open('задача1.tex', 'r', encoding='utf8')
lines = file_s_shablonom.readlines()
for line in lines:
    for perem in change:
        line = line.replace('!!!' + perem[0] + '!!!', str(perem[1]))
    file_dlya_zapisi.write(line)
file_dlya_zapisi.close()
file_s_shablonom.close()
