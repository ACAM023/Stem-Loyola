'''
 * Copyright: STEM Loyola
 * Date     : March 2019
 * ID       : 19.03-A2
 * Level    : 2 (Intermediate)
 *
 * Task     : The "numbers.txt" file contains 10,000 numbers. Jane has
 *            written the following program that displays all numbers on
 *            the screen. Your task is to improve the program so that
 *            when it is run, the program will display ONLY odd numbers
 *            and at the end display the total count of even numbers 
 *            contained in the file.
 *
 * Solved By: [
 		Name: Alvin Chris Mrema
 		Email: sonalpha023@gmail.com
 	]
'''

FILE_NAME = "numbers.txt"
TOTAL_NUMBERS = 10000


# Open the numbers file
try:
    numbersFile = open (FILE_NAME, "r")

except:
    # Terminate the program when the file could not be opened
    print ("Error: could not open the file \"{}\"".format(FILE_NAME))
    print ("Quitting...")

    exit(1)

# Initialize the Total count of Even Numbers and Odd counter
totalEven = 0
oddCount = 0

# Process the numbers' file and display results
for count in range(1, TOTAL_NUMBERS+1):
    number = int(numbersFile.readline())

    # Check for Odd and Even numbers
    if (number % 2 != 0):
    	oddCount += 1
    	print("{}: {}".format(oddCount, number))
    elif (number % 2 == 0):
    	totalEven += 1
    	
print("Total count of Even Numbers is {}".format(totalEven))

# Close open resources
numbersFile.close()
