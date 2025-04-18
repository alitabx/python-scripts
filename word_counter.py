counter = {}

try:
    sentence = input("Enter a sentence: ")
    if not sentence:
        raise ValueError("Empty input")

    lst = sentence.split()

    for item in lst:
        if item in counter:
            counter[item] += 1
        else: 
            counter[item] = 1

    print("Word counts: ", counter)
    with open('output.txt', 'w') as f:
        for k, v in counter.items():
            f.write(f"{k}:{v}\n")
    
except ValueError as e: 
    print(f'Something went wrong.\nDetails:\n{e}')

