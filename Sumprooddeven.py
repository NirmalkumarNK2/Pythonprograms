def calculate_sum_and_product(numbers):
    even_sum = 0
    odd_product = 1

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_product *= num

    return even_sum, odd_product

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

even_sum, odd_product = calculate_sum_and_product(numbers)

print(f"Sum of even numbers: {even_sum}")
print(f"Product of odd numbers: {odd_product}")