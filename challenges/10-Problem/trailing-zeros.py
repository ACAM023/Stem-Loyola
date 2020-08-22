def trailing_zeros(number):
    """
    i = len(number) - 1
    zeros = []

    while i >= 0:
        if number[i] == '0':
            zeros.append(number[i])
        
            if number[i] != number[i-1]:
                break
    
        i -= 1
    
    return len(zeros)
    """
    return len(number) - len(number.rstrip('0'))

number = input().strip()
    
print(trailing_zeros(number))
