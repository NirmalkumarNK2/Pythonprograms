def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_input = input("Enter the temperature in Celsius: ")
if celsius_input.replace('.', '', 1).isdigit():  
    celsius_input = float(celsius_input)
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input:.2f} Celsius is equal to {fahrenheit_output:.2f} Fahrenheit.")
else:
    print("Invalid input. Please enter a valid temperature in Celsius.")

