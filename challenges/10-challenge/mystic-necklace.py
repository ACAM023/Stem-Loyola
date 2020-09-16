def maximum_golds(beads):
    if "S" not in beads:
        return len(beads)
    
    max_gold = beads.count("G")
    limit = len(beads)
    
    for i in range(1, limit+1):
        start = 0
        while (start + i) < limit:
            temp = list(beads)
            for j in range(start, (i+start+1)):
                if temp[j] == "S":
                    temp[j] = "G"
                else:
                    temp[j] = "S"
            
            if "".join(temp).count("G") > max_gold:
                max_gold = "".join(temp).count("G")
            
            start += 1 
            
    return max_gold

beads = input().strip()

print(maximum_golds(beads))