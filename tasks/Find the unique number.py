def find_uniq(arr : list) -> int:
    # your code here
    a, b = set(arr)
    return a if arr[:3].count(a) <= 1 else b