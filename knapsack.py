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

n = len(items)
max_value = 0
best_items = []

start = time.perf_counter()

for bit in range(1 << n):
    total_capacity = 0
    total_value = 0
    selected = []

    for i in range(n):
        if bit & (1 << i):
            item_number, capacity, value = items[i]
            total_capacity += capacity
            total_value += value
            selected.append(item_number)

            if total_capacity <= max_capacity and total_value > max_value:
                max_value = total_value
                best_items = selected

end = time.perf_counter()

print("選んだ品物:", best_items)
print("最大値段:", max_value)
print(f"処理時間: {end - start:.6f} 秒")

