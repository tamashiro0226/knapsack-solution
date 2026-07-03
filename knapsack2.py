import time

items = [
    (1,4,6),
    (2,8,12),
    (3,3,4),
    (4,5,3),
    (5,9,7),
    (6,2,1),
    (7,3,3),
    (8,1,2),
    (9,5,7),
    (10,2,3),
    (11,4,4),
    (12,2,2),
    (13,7,10),
    (14,10,13),
    (15,3,5),
    (16,13,16),
    (17,11,14),
    (18,8,9),
]

max_capacity = 45

# dp[w] = 容量wで得られる最大価値
dp = [0] * (max_capacity + 1)

# choice[w] = 容量wで選んだ品物番号のリスト
choice = [[] for _ in range(max_capacity + 1)]

start = time.perf_counter()

for item_number, weight, value in items:
    for w in range(max_capacity, weight - 1, -1):
        if dp[w - weight] + value > dp[w]:
            dp[w] = dp[w - weight] + value
            choice[w] = choice[w - weight] + [item_number]

end = time.perf_counter()

print("選んだ品物:", choice[max_capacity])
print("最大値:", dp[max_capacity])
print(f"処理時間: {end - start:.6f} 秒")