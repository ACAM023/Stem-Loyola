def has_palindrome(number):
    limit = len(number)
    
    for i in range(2, limit+1):
        start = 0
        while (start + i) < limit:
            if number[start:(i+start)] == number[start:(start+i)][::-1]:
                return "YES"
            
            start += 1
        
    return "NO"
    """
    for i in range(len(number)):
        for j in range(i+2,len(number)+1):
            temp = number[i:j]
            if temp == temp[::-1]:
                return "YES"
    return "NO"
    """

number = input().strip()

print(has_palindrome(number))