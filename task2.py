"""Count the number of string elements in the list and output the result."""
items = [10, "Python", 3.14, True, "GitHub", [1, 2], 55, "SPbU"] #did you try to check this line with pycodestyle?

string_count = 0

for item in items:
    if type(item) is str:
        string_count += 1

print("List:", items)
print("Number of string elements:", string_count)
