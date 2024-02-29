user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

largest = max(numbers)
smallest = min(numbers)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
