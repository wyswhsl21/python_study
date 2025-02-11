data = [[1,2,3,4,5],[6,7,8900],[9,10,11,12,13],[14,1500,16,170]]

for row in range(len(data)):
    for col in range(len(data[row])):
        print(f'{data[row][col]:^5}', end= '\t')
    print()


    # 