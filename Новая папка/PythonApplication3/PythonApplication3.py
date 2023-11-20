import random

N = 5 # Размер квадрата
square = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)] # Создание квадрата и заполнение случайными числами

max_sum = [[0] * N for _ in range(N)]
min_sum = [[0] * N for _ in range(N)]

max_sum[0][0] = min_sum[0][0] = square[0][0]
for i in range(1, N):
    max_sum[0][i] = max_sum[0][i-1] + square[0][i]
    min_sum[0][i] = min_sum[0][i-1] + square[0][i]
    
for i in range(1, N):
    max_sum[i][0] = max_sum[i-1][0] + square[i][0]
    min_sum[i][0] = min_sum[i-1][0] + square[i][0]

for i in range(1, N):
    for j in range(1, N):
        max_sum[i][j] = max(max_sum[i-1][j], max_sum[i][j-1]) + square[i][j]
        min_sum[i][j] = min(min_sum[i-1][j], min_sum[i][j-1]) + square[i][j]

print(max_sum[N-1][N-1], min_sum[N-1][N-1])

