x1 = float(input('Cordenada X1 (0 ≤ X1 ≤ 10.000): '))
y1 = float(input('Cordenada Y1 (0 ≤ Y1 ≤ 10.000): '))

x2 = float(input('Cordenada X2 (0 ≤ X2 ≤ 10.000 e X1 < X2): '))
y2 = float(input('Cordenada Y2 (0 ≤ Y2 ≤ 10.000) e Y1 < Y2: '))

quatidade_met = int(input('Números de meteoros (0 ≤ N ≤ 10.000): '))
cordy = []
cordx = []

nCol = 0
for tmp in range(quatidade_met):
    cordx.append(float(input('Cordenada x do meteoro %d: ' % (tmp+1))))
    cordy.append(float(input('Cordenada y do meteoro %d: ' % (tmp+1))))
    if cordx[tmp] >= x1 and cordx[tmp] <= x2 and cordy[tmp] <= y1 and cordy[tmp] >= y2:
        nCol += 1


print('Numeros de meteoros que acertaram: %d' % nCol)