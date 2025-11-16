numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = []

for x in numbers:
    best = None
    best_diff = float('inf')
    for y in numbers:
        if numbers.count(x)<=1:
            if x == y:
                continue
        diff = abs(x-y)

        if diff < best_diff or (diff == best_diff and y < best):
            best = y
            best_diff = diff

    result.append(best)

print(result)

