import app
import math
from .util import check_types


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        check_types(x, y)
        return x + y

    def substract(self, x, y):
        check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        check_types(x, y)
        return x * y

    def divide(self, x, y):
        check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        check_types(x, y)
        return x ** y

    def sqrt(self, x):
        check_types(x)
        return math.sqrt(x)

    def log(self, x):
        check_types(x)
        return math.log10(x)


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
