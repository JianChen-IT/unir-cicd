# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def check_types(x, y=None):
    if x and y:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
    else:
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"
