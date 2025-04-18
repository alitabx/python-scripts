try: 
    input1 = input("Enter numbers:")
    if not input1:
        raise ValueError("Empty Value not allowed.")
    
    list1 = [int(x) for x in input1.split()]
    if len(list1) == 0:
        raise ValueError("Empty list not allowed.")
    stats = {}
    mean = sum(list1)/len(list1)
    
    list1.sort()
    median = 0
    if len(list1) % 2 == 0:
        i = len(list1)//2 - 1
        j = len(list1)//2
        median = (list1[i] + list1[j]) / 2
    else:
        index = len(list1) // 2
        median = list1[index]
    
    stats['mean'] = mean
    stats['median'] = median

    with open('stats.txt', 'w') as file:
        for k, v in stats.items():
            file.write(f"{k}:{v}\n")    

    with open('stats.txt', 'r') as file:
        print(file.read())

except ValueError as e:
    print(f"Invalid number: {e}")