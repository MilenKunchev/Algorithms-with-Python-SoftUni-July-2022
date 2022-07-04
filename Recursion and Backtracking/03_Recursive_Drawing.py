def drawing(num):
    if num == 0:
        return
    print('*' * num)
    drawing(num - 1)
    print('#' * num)



n = int(input())
drawing(n)
