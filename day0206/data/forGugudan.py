#

result = [x * y for x in range(1, 10) for y in range(1, 10)]
print(result, end=" ")
print()
for x in range(1, 10, 1):
    for y in range(1, 10, 1):
        result = ' '.join(str(x * y).zfill(2))
        # result = ' '.join(str(x * y))
        formatted_result = result.rjust(3)
        print(f'{x} * {y} = {formatted_result} ', end="\t")
    print()
