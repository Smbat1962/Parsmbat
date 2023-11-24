from datetime import date
import math

class NegativeValueError(Exception):
    pass


def positive_int(a):
    if a < 0 or type(a) == float:
        raise NegativeValueError


try:
    positive_int(-5)
except:
    print("the number is negativ")


def age(birth_date_year, birth_date_month, birth_date_day):
    today = date.today()
    y = today.year - birth_date_year
    if today.month < birth_date_month or today.month == birth_date_month and today.day < birth_date_day:
        y -= 1
    return y


try:
    positive_int(age(1962, 4, 29))
except:
    print("Incorrect input birth date")
else:
    print("Success input birt date")
    print(age(1962, 4, 29))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

try:
    key = "model"
    car[key]
except KeyError:
    print("The called key does not exist")
else:
    print("The called key name is ", car[key])


def division_errors(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("The denominator can not be zero")
    else:
        print("Result division equal  ", result)

def read_file(path):
    try:
        with open(path, "r") as f:
            f = open(path, "r")
    except FileNotFoundError:
        print("File does not exist")
    except IOError:
        print("Fails due to an input/output error")
    else:
        print("Execute if no exception", f)
    finally:
        print("Always executed")

def handling_errors(a, b, c):
    try:
        assert a != 0, "a can't be 0"
        D = (b * a - a * c)
        assert D >= 0, "Roots are imaginary"
        r1 = (-b / 3 + math.sqrt(D))/(2 * a)
        print("Roots of the quadratic equation are :", r1, "",D)
    except AssertionError as msg:
        print(msg)

class CustomError(Exception):
    pass

def custom_exception(a, b, c):
    if a + b <= c:
        raise CustomError

def triangle(x, y, z):
    try:
        custom_exception(x, y, z)
    except CustomError:
        print("Conditions do not met") 
    else:
        print("Conditions do met")




def main():
    read_file("C:\\Users\\Admin\\Downloads\\my_xem.txt")
    division_errors(7, 0)
    handling_errors(2, 5, -6)
    handling_errors(0, 1, 6)
    handling_errors(2, 12, 18)
    triangle(12, 25, 9)
    triangle(17, 35, 219)


if __name__ == "__main__":
    main()
