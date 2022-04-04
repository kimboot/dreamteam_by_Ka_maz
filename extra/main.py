#extra tasks l1.20-l1.24

def zero():
    for x in (True, False):

        for y in (True, False):

         for z in (True, False):

             result = not (y or not x and z) or z
             result2 = not(x or not y and z)
             result3 = x and not (not y or z) or y
             result4 = not (x and not y) or (x or not z)
             result5 = not (x or y) and (not x or not z)
             print(f'1 ({x=},{y=},{z=}) = {result}')
             print(f'2 ({x=},{y=},{z=}) = {result2}')
             print(f'3 ({x=},{y=},{z=}) = {result3}')
             print(f'4 ({x=},{y=},{z=}) = {result4}')
             print(f'5 ({x=},{y=},{z=}) = {result5}')

print(zero())