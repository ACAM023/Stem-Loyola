import os


LOGS_FILENAME  = "logs.txt"


# File used to log status and error messages
logFile = None


# Setup a custom file for writing logs and statuses
def setupLogs ():
    global logFile
    logFile = open(LOGS_FILENAME, "w")


# Display a message to the user. By default, end is a new line character
def display ( message, end = "\n" ):
    print(message, end=end)


# Save a message to a logs file. By default, end is a new line character
def log ( message, end = "\n" ):
    global logFile
    logFile.write(message)
    logFile.write(end)


# Display a message to the user and save the message to a logs file. By 
# default, end is a new line character
def displayAndLog ( message, end = "\n" ):
    global logFile
    logFile.write(message)
    logFile.write(end)

    print(message, end=end)
