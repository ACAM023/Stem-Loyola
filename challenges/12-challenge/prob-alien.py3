bases_number = int(input().strip())
continous_positive = 0
scores = []

for i in range(bases_number):
    charge = int(input().strip())
    
    scores.append(continous_positive + charge)
    
    if (charge + continous_positive) >= 0:
        continous_positive += charge
    else:   
        continous_positive = 0

highest_score = 0

for score in scores:
    if score > highest_score:
        highest_score = score

print(highest_score)