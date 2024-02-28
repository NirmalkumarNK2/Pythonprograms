def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

a = input("Enter a string: ")
if is_palindrome(a):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")