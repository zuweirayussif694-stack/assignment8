my_list = ['apple', 'banana', 'cherry', 'date', 'banana']
print(f"Initial List: {my_list}")

# 1. del() Operation:
# Delete the element at index 2 (which is 'cherry')
del my_list[2]
print(f"After del my_list[2]: {my_list}")

# 2. append() Operation:
# Add 'grape' to the end of the list
my_list.append('grape')
print(f"After append('grape'): {my_list}")

# 3. extend() Operation:
# Extend the list with another list ['kiwi', 'lemon']
my_list.extend(['kiwi', 'lemon'])
print(f"After extend(['kiwi', 'lemon']): {my_list}")

# 4. insert() Operation:
# Insert 'orange' at index 1
my_list.insert(1, 'orange')
print(f"After insert(1, 'orange'): {my_list}")

# 5. pop() Operation:
# Remove and return the last element
popped_item = my_list.pop()
print(f"After pop(): {my_list}, Popped Item: {popped_item}")

# 6. remove() Operation:
# Remove the first occurrence of 'banana'
my_list.remove('banana')
print(f"After remove('banana'): {my_list}")
my_list.remove("banana")
print(f"After remove('banana'): {my_list}")
#7. reverse() Operation:
# Reverse the order of elements in the list
my_list.reverse()
print(f"After reverse(): {my_list}")
#8. sort() Operation:
# Sort the list alphabetically
my_list.sort()
print(f"After sort(): {my_list}")