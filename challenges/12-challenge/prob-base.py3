genetic_code = input().strip()

base_pair = {'CG': 0, 'AT': 0}

index = 1
while (index < len(genetic_code)):
    if genetic_code[index-1: index+1] == 'CG':
        base_pair['CG'] += 1
        index += 1
    elif genetic_code[index-1: index+1] == 'AT':
        base_pair['AT'] += 1
        index += 1
    
    index += 1

if (base_pair['AT'] > 0) and (base_pair['CG'] > 0):
    if (base_pair['AT'] == base_pair['CG']):
        print('EQUAL')
    elif (base_pair['AT'] > base_pair['CG']):
        print('A-T')
    elif (base_pair['AT'] < base_pair['CG']):
        print('C-G')
else:
    print('NO')
