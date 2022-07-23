def draw(count, spaces_count):
    if count == 0:
        return
    spaces = ' ' * spaces_count
    stars = '*' * count
    print(spaces + stars)

    draw(count - 2, spaces_count + 1)

    spaces = ' ' * spaces_count
    stars = '*' * count
    print(spaces + stars)


draw(12, 0)
