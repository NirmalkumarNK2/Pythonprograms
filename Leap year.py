def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

user_input = int(input("Enter a year: "))
if is_leap_year(user_input):
    print(user_input, "is a leap year.")
else:
    print(user_input, "is not a leap year.")