def format_name(f_name, l_name):
    """Take a first and last name and format it to return the"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


def my_function(num):
    """Add one to the number passed in and return the result."""
    if type(num) != int:
        return "Please enter a number"
    else:
        return num + 1
