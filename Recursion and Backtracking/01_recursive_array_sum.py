def calc_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + calc_sum(numbers, idx + 1)


nums = [int(x) for x in input().split()]

print(calc_sum(nums, 0))
