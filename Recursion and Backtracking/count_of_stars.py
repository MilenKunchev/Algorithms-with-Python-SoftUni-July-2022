arr = ['0', '1', '*', '3', '*', '5', '*', '7', ]


def count_stars(idx, count, positions, arr):
    if idx >= len(arr):
        print(f'count of "*": {count}')
        print(f'at positions {"; ".join(str(x) for x in positions)}')
        return
    if arr[idx] == '*':
        count += 1
        positions.append(idx)
    count_stars(idx + 1, count, positions, arr)


count_stars(0, 0, [], arr)
