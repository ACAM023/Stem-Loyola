genetic_code = input().strip()

result = 'YES'
necessary = 'ACGT'

for code in genetic_code:
    if code not in necessary:
        result = 'NO'
        break
    
print(result)
