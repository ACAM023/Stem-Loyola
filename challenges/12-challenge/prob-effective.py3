bases_number = int(input().strip())

group_members = []
groups = []

for i in range(bases_number):
    charge = int(input().strip())
    
    if (len(group_members) != 0):
        if (((group_members[-1] > 0) and (charge < 0)) or
        ((group_members[-1] < 0) and (charge > 0))):
            groups.append(sorted(group_members))
            group_members = []
    
    group_members.append(charge)
    
    if i == bases_number-1:
        groups.append(sorted(group_members))

for group in groups:
    for member in group:
        print(member)
