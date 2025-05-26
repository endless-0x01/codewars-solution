def find_next_square(sq):
    if sq < 0:
        return -1
    
    x = 0
    while x ** 2 <= sq:
        if x ** 2 == sq:
            return (x + 1) ** 2
        x += 1
    else:
        return -1