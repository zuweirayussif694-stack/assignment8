my_dictionary = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"color": "red"
}
print(f"Initial Dictionary: {my_dictionary}")
#Instructions:
#1. Access Specific Value by Key:
# Access the value associated with the key "model"
model_name = my_dictionary["model"]
print(f"Model: {model_name}")
# Access the value associated with the key "year"
year_value = my_dictionary["year"]
print(f"Year: {year_value}")
#2. Access Keys, Values, and Items of Dictionary:
# Get all keys
all_keys = my_dictionary.keys()
print(f"All Keys: {list(all_keys)}") # Convert to list for clear display
# Get all values
all_values = my_dictionary.values()
print(f"All Values: {list(all_values)}") # Convert to list for clear display
# Get all key-value pairs (items)
all_items = my_dictionary.items()
print(f"All Items: {list(all_items)}") # Convert to list for clear display
#3. Add/Change Dictionary Items:
# Add a new key-value pair "engine": "V8"
my_dictionary["engine"] = "V8"
print(f"After adding 'engine': {my_dictionary}")
# Change the value of "color" to "blue"
my_dictionary["color"] = "blue"
print(f"After changing 'color': {my_dictionary}")
#4. Remove Dictionary Items (pop() and del):
# Remove the item with the key "year" using pop()
removed_year = my_dictionary.pop("year")
print(f"After pop('year'): {my_dictionary}, Removed Year:{removed_year}")
# Remove the item with the key "brand" using del
del my_dictionary["brand"]
print(f"After del my_dictionary['brand']: {my_dictionary}")
#5. Length of a Dictionary (len()):
# Get the number of key-value pairs in the dictionary
dictionary_length = len(my_dictionary)
print(f"Length of the dictionary: {dictionary_length}")
#6. clear() Operation (Optional, as it clears all):
# Remove all items from the dictionary
my_dictionary.clear()
print(f"After clear(): {my_dictionary}")
