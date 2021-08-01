time, temp, unit = input().strip().split(' ')
result = 'BAD'

if (int(time) <= 12):
    if (unit == 'C' and (int(temp) >= 9 and int(temp) <= 25)):
        result = 'GOOD'
    elif (unit == 'F' and (int(temp) >= 48 and int(temp) <= 77)):
        result = 'GOOD'

print(result)
