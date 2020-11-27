# Three ways to remove an item from a list in python:

data = ["Apple", "Banana", "Cherry", "Durian", "Pineapple"]

print("INITIAL:", data)  # INITIAL: ['Apple', 'Banana', 'Cherry', 'Durian', 'Pineapple']

data.remove("Durian")

print("SANS-DURIAN:", data)  # INITIAL: ['Apple', 'Banana', 'Cherry', 'Pineapple']

removed_item = data.pop()  # pop with no arguments returns and removes the last item.

print("POST_POP:", data)  # INITIAL: POST_POP: ['Apple', 'Banana', 'Cherry']

removed_item = data.pop(0)  # You can specify the index including 0 to remove the first item.

print("POST_POP_FIRST:", data)  # POST_POP_FIRST: ['Banana', 'Cherry']

del data[1]  # removes the item at the index (1 specifies the second item in this case) but does not return the item.

print("POST_DEL:", data)  # POST_POP_FIRST: ['Banana']
