def range(min=None, max=None, step=None):
    if min is not None and max is not None and step is None:
        i = min
        result = []
        while i < max:
            result.append(i)
            i += 1
        return result
    elif min is not None and max is not None and step is not None:
        i = min
        result = []
        while i < max:
            result.append(i)
            i += step
        return result
    elif min is None and max is not None and step is None:
        i = 0
        result = []
        while i < max:
            result.append(i)
            i += 1
        return result
    else:
        return "invalid parameters"


print(f'1 {range(1, 10)}')
print(f'2 {range(1, 10, 2)}')
print(f'3 {range(max=10)}')
print(f'4 {range(None, 10)}')
print(f'5 {range(None, 10, -1)}')