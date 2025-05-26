def find_it(seq : list):
    result = 0
    for num in seq:
        result ^= num
    return result