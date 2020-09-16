'''
 * Copyright: STEM Loyola
 * Date     : May 2019
 * ID       : 19.05-A2
 * Level    : 2 (Intermediate)
 *
 * Task     : As the legend goes, a mysterious list of 100,000 numbers was
 *            discovered at Nungwi (the northernmost part of Unguja island).
 *            As neither the origin nor the purpose of the numbers were ever
 *            ascertained, a Mathematics professor from the University of
 *            Dar es Salaam spent one weekend analyzing the list for any
 *            interesting information. After two days of intensive work, the
 *            professor realized that the list contains only 777 prime numbers.
 *            For unknown reasons, she called these 777 numbers as the
 *            forbidden primes.
 *            You are given the entire list of 100,000 numbers (each number on
 *            its own line) and your task is to find the largest of the
 *            forbidden primes. Extra credit shall be awarded if you can find
 *            the ten (10) largest forbidden primes from the list.
 *
 *            Note: Your program should take less than 777 seconds to find the
 *                  solution. Extra credit shall be awarded for programs that
 *                  take less than 7 seconds.
 *
 *
 * Solved By: <Full Name> - <Email Address>
 *     Class: <Form> - <Stream/Combination>
'''

FILE_NAME = "forbidden-list.txt"


# Open the numbers file
try:
    resultsFile = open (FILE_NAME, "r")

except:
    # Terminate the program when the file could not be opened
    print ("Error: could not open the file \"{}\"".format(FILE_NAME))
    print ("Quitting...")

    exit(1)

# Function that checks if a number is Prime
def isPrime(number):
    if number % 2 == 0:
        return False
    if number == 2:
        return True
    
    limit = float(pow(number, 0.5) + 1)
    divider = 3
        
    while divider <= limit:
        if number % divider == 0:
            return False
        divider += 2
        
    return True

# Useful variables
primeNumbers = []
count = 0

# Process the numbers file
for line in resultsFile:
    num = int(line.strip())

    # print(num)
    if isPrime(num):
        count += 1
        primeNumbers.append(num)
        
topPrime = sorted(primeNumbers, reverse=True)[:10]

for prime in topPrime:
    print(prime)
print("There are {} Prime Numbers".format(count))

# Close open resources
resultsFile.close()
