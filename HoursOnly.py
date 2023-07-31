
def days_to_units(no_of_days):
    return f"{no_of_days} days is {no_of_days * 24} hours"


def validate_and_convert(user_input):
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            corrected_value = days_to_units(user_input_number)
            print(corrected_value)
        elif user_input_number == 0:
            print(f"No of days cannot be zero")
        else:
            print(f"No of days cannot be negative")

    except ValueError:
        print(f"Entered value is not supported")

