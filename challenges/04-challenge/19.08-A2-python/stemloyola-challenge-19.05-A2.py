'''
 * Copyright: STEM Loyola
 * Date     : May 2019
 * ID       : 19.08-A2
 * Level    : 2 (Intermediate)
 *
 * Task     : Over the June holiday, Luke went to visit his grandparents living
 *            at Songambele in Dodoma. When he was few minutes from getting off
 *            the bus, he overheard one lady behind him that she was born at
 *            Songambele ward in Kagera. Luke wondered how many wards are 
 *            called Songambele in Tanzania. After searching online, he found
 *            out that there are four wards in Tanzania called Songambele: in
 *            Kongwa (Dodoma), Urambo (Tabora), Kyerwa (Kagera) and Kiteto (Manyara).
 * 
 *            After returning to school, Luke has been searching for ward names
 *            that have been reused for more than four times. All he could find
 *            are other ward names like Magomeni, Malolo, Mbuyuni and Mjimwema
 *            that have also been reused four times. Luke has downloaded a list
 *            of all ward names in Tanzania (almost 3,650 wards) and needs your
 *            help to find all the ward names that have been reused for more
 *            than four times.
 * 
 *            Note: (1) Each ward is on its own line.
 *                  (2) Some ward names like "Arusha Chini" contain spaces.
 * 
 *            Fun Fact: The most famous ward name has been reused fourteen times.
 *
 * Solved By: <Alvin>
 *     Email: <sonalpha023@gmail.com>
 *     Form : <Alumni>
 *    Stream: <PCM>
'''

FILE_NAME = "tanzania-wards.txt"

# Open the wards file
try:
    wardsFile = open (FILE_NAME, "r")

except:
    # Terminate the program when the file could not be opened
    print ("Error: could not open the file \"{}\"".format(FILE_NAME))
    print ("Quitting...")

    exit(1)

wards = {}

# Process the wards file
for line in wardsFile:
    ward = line.strip()
    
    # print(ward)

    if line not in wards:
        wards[line] = 1
    else:
        wards[line] += 1

for ward, count in wards.items():
    if count > 4:
        print(ward + " has " + str(count) + " count")

# Close open resources
wardsFile.close()
