def knapsack(items, max_weight):
    table = list()

    for i in range(len(items)+1):
        table.append(list())
        for j in range(max_weight+1):
            table[i].append(0)

    for i in range(1, len(items)+1):
        for j in range(1, max_weight+1):
            if j < items[i]['weight']:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-items[i]['weight']] + items[i]['value'])

    return table[len(items)][max_weight]

items = {
    1: {'weight': 10, 'value': 60},
    2: {'weight': 20, 'value': 100},
    3: {'weight': 30, 'value': 120}
    }

print(knapsack(items, 50))