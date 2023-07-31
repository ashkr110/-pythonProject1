# Function to convert days to units for multiple conversion units
def days_to_units_dict(no_of_days, name_of_unit):
    if name_of_unit == "hours":
        return f"{no_of_days} days is {no_of_days * 24} {name_of_unit}"
    elif name_of_unit == "minutes":
        return f"{no_of_days} days is {no_of_days * 24 * 60} {name_of_unit}"
    elif name_of_unit == "seconds":
        return f"{no_of_days} days is {no_of_days * 24 * 60 * 60} {name_of_unit}"
    else:
        return "Unsupported conversion unit"


def validate_and_convert_dict(user_input_dictionary):
    try:
        user_input_number = int(user_input_dictionary["days"])
        if user_input_number > 0:
            corrected_value = days_to_units_dict(user_input_number, user_input_dictionary["unit"])
            print(corrected_value)
        elif user_input_number == 0:
            print(f"No of days cannot be zero")
        else:
            print(f"No of days cannot be negative")

    except ValueError:
        print("Entered value is not supported")
    except TypeError:
        print("Value of days must be in numbers")


def conversion_to_dictionary(input_to_be_converted):
    input_split = input_to_be_converted.split(":")
    try:
        return {"days": input_split[0], "unit": input_split[1]}
    except IndexError:
        return "Enter conversion unit"


