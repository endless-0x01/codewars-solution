def sum_strings(x : str, y : str):
    a = x.lstrip('0') or '0'
    b = y.lstrip('0') or '0'

    digits_a = list(a)
    digits_b = list(b)

    i = len(digits_a) - 1
    j = len(digits_b) - 1

    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_a = int(digits_a[i]) if i >= 0 else 0
        digit_b = int(digits_b[j]) if j >= 0 else 0


        total = digit_a + digit_b + carry
        carry = total // 10
        result.append(str(total % 10))
    
        i -= 1
        j -= 1

    result_str = ''.join(reversed(result))

    return result_str.lstrip('0') or '0'