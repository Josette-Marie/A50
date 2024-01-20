# Add intergers of idefinite size

def add_strings(num1, num2):
    result = []
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(num1[i])
            i -= 1
        if j >= 0:
            total += int(num2[j])
            j -= 1
        result.append(str(total % 10))
        carry = total // 10

    return ''.join(result[::-1])

# Example usage
number1 = "123456789012345678901234567890"
number2 = "987654321098765432109876543210"
sum_of_numbers = add_strings(number1, number2)
print(sum_of_numbers)