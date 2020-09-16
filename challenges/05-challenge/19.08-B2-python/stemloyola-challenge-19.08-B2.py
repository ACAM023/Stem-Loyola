'''
 * Copyright: STEM Loyola
 * Date     : August 2019
 * ID       : 19.08-B2
 * Level    : 2 (Intermediate)
 *
 * Task     : In 2014, NECTA released the form four (CSEE) results in GPA and
 *            class format (Figure 2). This came after they had introduced "B+"
 *            and "E" grades during the 2013 results. Your task is to convert
 *            the results to the points and divisions format (Figure 3) that we
 *            are all familiar with and count students in each division. A text
 *            file "2014-CSEE-S0800.txt" contains the results in GPA format as
 *            shown in Figure 1. No one got division zero but we have added one
 *            division-zero results to ensure you write a complete program.
 *
 *      Note: (1) Points and divisions are calculated from the 7 best grades as
 *                shown in Figure 4 and Figure 5.
 *            (2) In order to get Division IV, a student must have at least
 *                2 Ds or 1 C. This means, for example, that 6 Es and 1 D
 *                (i.e. 41 pts) will still be Division 0.
 *
 * Solved By: <Alvin>
 *     Email: <sonalpha023@gmail.com>
 *     Form : <Alumni>
 *    Stream: <PCM>
'''

FILE_NAME = "2014-CSEE-S0800.txt"

# Open the results file
try:
    resultsFile = open (FILE_NAME, "r")

except:
    # Terminate the program when the file could not be opened
    print ("Error: could not open the file \"{}\"".format(FILE_NAME))
    print ("Quitting...")

    exit(1)

# Parse the results files and extract students data
for line in resultsFile:
    # Extract the student ID and gender
    line = line.strip()
    items = line.split(' ', 2)
    
    studID = items[0]
    gender = items[1]
    
    print(studID, gender, end=": ")  # For debugging
    
    # Extract all available subjects
    results = line[13:].split("'")
    grades = results[1::2]
    print(grades)   # For debugging
    
    

# Close open resources
resultsFile.close()
