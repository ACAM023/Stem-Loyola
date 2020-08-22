def deep_zeros(number):
    i = len(number) - 1
    zeros = []
    
    if i <= 2:
        return 0

    while i >= 0:
        if number[i] == '0' and number[i] != number[i-1]:
            zeros.append(number[i])
    
        i -= 1
        
    return len(zeros)

number = input()
    
print(deep_zeros(number))