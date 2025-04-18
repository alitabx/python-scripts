
try:
    input1 = input("Enter first set:")
    input2 = input("Enter second set:")

    if not set1 or not set2:
        raise ValueError("Sets should not be empty.")

    list1 = [int(i) for i in set1.split()]
    list2 = [int(i) for i in set2.split()]
    set1 = set(set1)
    set2 = set(set2)
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1.union(set2)}")
    print(f"Intersection: {set1.intersection(set2)}")

    with open('sets.txt', 'w') as file:
        file.write(f"Union:{" ".join(map(str, set1.union(set2)))}\n")
        file.write(f"Intersection:{" ".join(map(str, set1.intersection(set2)))}")

    with open('sets.txt', 'r') as file:
        print(file.read())

except ValueError as e:
    print(f"Enter numbers only: {e}")