n, m = map(int, input().strip().split(' '))

line = ""

for j in range(n):
    line = line + '*'

for i in range(m):
    print(line)