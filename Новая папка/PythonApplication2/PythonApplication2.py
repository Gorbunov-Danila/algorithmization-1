
count = m = 0
with open('1.txt') as file:
    f = file.read()
    f = list (map(int,f.split()))
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] + l[j]) % 120 == 0:
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)
