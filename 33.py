# Sum Numbers in a comma delimited string

def sum_of_numbers_in_string(numbers_string):
    numbers = numbers_string.split(',')
    sum_of_numbers = sum(int(num) for num in numbers)
    return sum_of_numbers

# Example usage
input_numbers = "10,20,30,40,50"
total_sum = sum_of_numbers_in_string(input_numbers)
print("Sum of numbers:", total_sum)
