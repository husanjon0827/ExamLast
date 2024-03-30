def plus_one(digits):
    n = len(digits)
    carry = 1

    # Traverse the digits from right to left
    for i in range(n - 1, -1, -1):
        # Add the carry to the current digit
        digits[i] += carry
        # Check if there's a carry
        if digits[i] == 10:
            # Set current digit to 0
            digits[i] = 0
            # Set carry to 1 for the next iteration
            carry = 1
        else:
            # If no carry, exit the loop
            carry = 0
            break

    # If there's still a carry after the loop, insert 1 at the beginning
    if carry:
        digits.insert(0, 1)

    return digits

# Example usage:
digits = [9, 9, 9]
print(plus_one(digits))  # Output: [1, 0, 0, 0]
