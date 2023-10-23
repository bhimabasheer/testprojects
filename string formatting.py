person_info = ["Alice", 30, "New York"]


formatted_string_1 = ["Name: {0}, Age: {1}, City: {2}".format(person_info[0], person_info[1], person_info[2])]
print(formatted_string_1)


formatted_string_2 = [f"Name: {person_info[0]}, Age: {person_info[1]}, City: {person_info[2]}"]
print(formatted_string_2)