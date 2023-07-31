from Dictionary import *
from HoursOnly import *

user_input = ""
input_to_dictionary = ""
while user_input != "exit":
    user_input = input("Enter the number of days (and Units)\n")
    if user_input.__contains__(":"):
        user_input_dictionary = conversion_to_dictionary(user_input)
        validate_and_convert_dict(user_input_dictionary)
    else:
        validate_and_convert(user_input)


