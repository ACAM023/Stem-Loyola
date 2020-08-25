def mike_puzzle(contacts, first, second):
    people = []
    i = 0
    while i < contacts:
        row = [*map(int, input().split())]
        people.append(row)
        
        i += 1
    
    score = 0
    index = 0
    
    return score
    

contacts = int(input().strip())

first, second = map(int, input().split())

print(mike_puzzle(contacts, first, second))