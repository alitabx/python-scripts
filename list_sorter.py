# This function will return the new array with sorted items.
def r_sorter(arr):
    seen = {}
    sorted_arr = []
    index_holder = 0
    step = 0
    while index_holder < len(arr):
 
        cur_num = arr[index_holder]

        if seen.get(cur_num) != None:
            index_holder += 1
            continue

        for item in arr:
            step += 1
            if seen.get(item) == None and item < cur_num:
                cur_num = item

        seen[cur_num] = True
        sorted_arr.append(cur_num)

    print(step)
    return sorted_arr


# This function will sort input array in place without returning new array
def sorter(arr):
    for item in range(len(arr)):
        for position in range(item, len(arr)):
            if arr[item] > arr[position]:
                arr[item], arr[position] = arr[position], arr[item]


# Input section
try:
    number_list = input("Enter values to sort: ")   

    if not number_list:
        raise ValueError("Empty input.")

    arr = number_list.split()

    # Convert str to int
    for item_index in range(len(arr)):
        arr[item_index] = int(arr[item_index])

    # Process array
    sorter(arr)
    print(arr)

    # Write to file
    with open('sorted.txt', 'w') as file:
        file.write(' '.join(map(str, arr)))
        

    
    # Read from file
    # with open('sorted.txt', 'r') as file:
    #     result = file.read()
    #     print(result)


except ValueError as e:
    print(f"Invalid number.\nDetails: {e}")
