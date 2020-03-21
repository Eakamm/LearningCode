n = input()

l = len(n)
m = n[:l - 1]
if '.' in m:
    m = float(m)
else:
    m = int(m)
if 'F' in n:
    c = (m - 32) / 1.8
    print('%.2f' % c + 'C')
else:
    f = m * 1.8 + 32
    print('%.2f' % f + 'F')