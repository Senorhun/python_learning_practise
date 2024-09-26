def pythagoras_number_trio_find(max):
    result = []
    for x in range(1, max+1):
        for y in range(x,max+1):
            for z in range(y,max+1):
                if x*x + y*y == z*z:
                    if x % 3 != 0 and y % 4 != 0 and z % 5 != 0:
                        result.append((x,y,z))
    return result

print(pythagoras_number_trio_find(20))