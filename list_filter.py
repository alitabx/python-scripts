

def lst_filter(arr, filter):
    return [x for x in arr if x > filter]


try:
    lst_input = input("Enter numbers: ")
    filter_input = int(input("Enter a number to filter a list based on: "))
    if not lst_input:
        raise ValueError("Empty input.")

    # Converting to numbers
    numbers = [int(x) for x in lst_input.split()]

    # filtering list
    result = lst_filter(numbers, filter_input)
    print(f"filtered: {result}")

    # Write to file 
    with open('filtered.txt', 'w') as file:
        file.write(" ".join(map(str, result)))

    # Read file
    with open('filtered.txt', 'r') as file:
        lines = file.read()
        print(lines)

except ValueError as e:
    print(f"Invalid Input: {e}")
