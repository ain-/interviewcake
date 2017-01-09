

def calculate_best(values):
    min_sell = (len(values) - 1) * [None]
    current_min = values[0]
    for i in range(0, len(min_sell)):
        current_min = min(current_min, values[i])
        min_sell[i] = current_min
    max_buy = (len(values) - 1) * [None]
    current_max = values[len(values) - 1]
    for i in range(len(max_buy) - 1, -1, -1):
        current_max = max(current_max, values[i + 1])
        max_buy[i] = current_max
    return max(zip(max_buy, min_sell), key=lambda x: x[0] - x[1])


prices = list(map(int, input().split()))
sell, buy = calculate_best(prices)
print(sell - buy)
