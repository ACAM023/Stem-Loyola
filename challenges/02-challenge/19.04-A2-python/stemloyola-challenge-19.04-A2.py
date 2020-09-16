'''
 * Copyright: STEM Loyola
 * Date     : April 2019
 * ID       : 19.04-A2
 * Level    : 2 (Intermediate)
 *
 * Task     : You are given a text file containing the 2018 Form Four results
 *            for Loyola. On eachline: a student ID, gender and his/her NECTA
 *            points are given. Complete the provided program to count how many
 *            students got each of the points. That is, if available: howmany 
 *            students got 7 points, how many got 8 points, etc. As an example,
 *            below is the count of the last four points.
 *            
 *                    25 points: 3 students
 *                    26 points: 3 students
 *                    29 points: 2 students
 *                    30 points: 1 student
 *           
 *            Bonus points will be given if your program will also list the
 *            respective students as shown below.   
 * 
 *                    25 points: 3 students (S0800/0071, S0800/0089, S0800/0101)
 *                    26 points: 3 students (S0800/0003, S0800/0054, S0800/0115)
 *                    29 points: 2 students (S0800/0072, S0800/0118)
 *                    30 points: 1 student (S0800/0110)
 *
 * 
 * Solved By: [
 		Name: Alvin Chris Mrema
 		Email: sonalpha023@gmail.com
 	]
'''

FILE_NAME = "2018-CSEE-S0800.txt"


# Open the numbers file
try:
    resultsFile = open (FILE_NAME, "r")

except:
    # Terminate the program when the file could not be opened
    print ("Error: could not open the file \"{}\"".format(FILE_NAME))
    print ("Quitting...")

    exit(1)

divisionPoints = {}

# Process the results file
for line in resultsFile:
    items = line.split()
    
    studentID = items[0]
    gender = items[1]
    points = int(items[2])
    
    if points not in divisionPoints.keys():
        divisionPoints[points] = [1, []]
    elif points in divisionPoints.keys():
        divisionPoints[points][0] += 1
    divisionPoints[points][1].append(studentID)

    # print("{} {} {}".format(studentID, gender, points))

for key, value in sorted(divisionPoints.items()):
    if value[0] == 1:
        print("{} points: {} student ('{}')".format(key, value[0], value[1][0]))
    else:
        print("{} points: {} students {}".format(key, value[0], tuple(value[1])))

# Close open resources
resultsFile.close()
