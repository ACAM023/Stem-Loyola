def deep_zeros(number):
    """
    i = len(number) - 1
    zeros = []
    
    if i <= 2:
        return 0

    while i >= 0:
        if number[i] == '0' and number[i] != number[i-1]:
            zeros.append(number[i])
    
        i -= 1
        
    return len(zeros)
    """
    
    return len(number) - (len(number) - len(number.rstrip('0'))) - len([x for x in number if x != '0'])

number = input().strip()
    
print(deep_zeros(number))