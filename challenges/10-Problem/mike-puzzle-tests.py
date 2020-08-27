import unittest

def mike_puzzle(contacts, first, second, people):
    """
    people = []
    i = 0
    while i < contacts:
        row = [*map(int, input().split())]
        people.append(row)
        
        i += 1
    """
    
    score = 0
    row = 0
    col = 0
        
    if people[first-1][second-1] == people[second-1][first-1]:
        if people[first-1][second-1] < 14:
            return "YES"
        else:
            return "NO"
    
    while col < contacts or row < contacts:
        if people[row][col] == 0:
            col += 1
            continue
        elif people[row][col] in people[first-1] and people[row][col] == people[col][row]:
            if people[col][second-1] == people[second-1][col]:
                if people[col][second-1] != 0:
                    score += people[col][second-1] + people[col][row]
                
                    if score < 14:
                        return "YES"
                    else:
                        score = 0
                        col += 1
                        continue
                else:
                    for member in people[second-1]:
                        if member == 0:
                            continue
                        
                        position = people[second-1].index(member)
                        if people[position][col] != 0 and people[col][position] == people[position][col]:
                            score += people[position][col] + people[col][row] + member
                            
                            if score < 14:
                                return "YES"
                        else:
                            continue
    
    return "NO"

"""
contacts = int(input().strip())

first, second = map(int, input().split())

print(mike_puzzle(contacts, first, second))
"""

people = [
        [0,10,0,13,2,0],
        [10,0,6,0,0,0],
        [0,6,0,5,0,0],
        [13,0,5,0,3,17],
        [2,0,0,3,0,0],
        [0,0,0,17,0,0]
    ]

class TestStringMethods(unittest.TestCase):

    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 1, 3, people), "YES")
        
    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 1, 2, people), "YES")
        
    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 1, 5, people), "YES")
        
    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 1, 4, people), "YES")
        
    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 4, 6, people), "NO")
        
    def test_mike_puzzle(self):
        self.assertEqual(mike_puzzle(6, 1, 6, people), "NO")

if __name__ == '__main__':
    unittest.main()