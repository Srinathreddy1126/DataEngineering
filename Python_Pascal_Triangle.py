n = 10
row = [1]
print(row)
for i in range(1,n):
    next_row = [1]
    for j in range(i-1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)
    row = next_row
    print(row)