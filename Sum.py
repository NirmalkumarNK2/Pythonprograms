user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
list_sum = sum(numbers)
print("Sum of all elements in the list:", list_sum)