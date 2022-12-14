x = 0
y = 1
s = 0

print(x, y, end=' ')

for i in range(13):
    s = x + y
    print(s, end=' ')
    x = y
    y = s