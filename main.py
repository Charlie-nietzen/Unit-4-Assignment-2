from rich.console import Console
from rich.table import Table

import os


def readFile(dataSource):
    dataSource = open(dataSource, "r")  # open file
    dataIn = dataSource.read()
    dataSource.close()
    dataIn = eval(dataIn)  # convert dataIn to a list
    return dataIn


def writeFile(dataSource, data):
    dataSource = open(dataSource, "w")
    data = str(data)  # convert data to a string
    dataSource.write(data)  # update the file with the new data
    dataSource.close()


def getAverage(dataSource):
    data = readFile(dataSource)

    for student in data:
        student[6] = round((int(student[3]) + int(student[4]) + int(student[5])) / 3)  # uses python's round() function
        # to get an integer value
    writeFile(dataSource, data)


def fieldKeys():
    print("Key for Sorting:\n1: ID\n2: First Name\n3: Last Name\n4: Score 1\n5: Score 2\n6: Score\n7: Average")


def clearScreen():
    os.system('cls||clear')  # clears the screen


def displayData(dataSource, data=None, leaderboard=False):
    dataTable = Table()

    rank = 1

    if leaderboard:
        dataTable.add_column("Rank", justify="right")  # if creating a leaderboard, add the rank column

    dataTable.add_column("ID"), dataTable.add_column("First Name"), dataTable.add_column("Last Name")

    if not leaderboard:
        dataTable.add_column("Score 1"), dataTable.add_column("Score 2"), dataTable.add_column("Score 3")

    dataTable.add_column("Average")

    if data is None:  # if data is empty, read the data from the file
        data = readFile(dataSource)

    for student in data:
        studentOut = []
        for item in student:
            studentOut.append(item)
        if leaderboard:
            dataTable.add_row(str(rank), studentOut[0], studentOut[1], studentOut[2], str(studentOut[6]))
            rank += 1
        else:
            dataTable.add_row(studentOut[0], studentOut[1], studentOut[2], str(studentOut[3]), str(studentOut[4]),
                              str(studentOut[5]), str(studentOut[6]))

    console = Console()
    console.print(dataTable)


def displaySorted(dataSource, leaderboard=False):
    data = readFile(dataSource)
    fieldKeys()  # prints out the options for sorting
    if leaderboard:
        fieldToSort = 7  # sort by average score if presenting leaderboard
    else:
        fieldToSort = input("Sort Records by which Field: ")
    fieldToSort = int(fieldToSort)
    sortedList = sorted(data, key=lambda studentNum: studentNum[fieldToSort - 1], reverse=True)  # sorts the data by
    # the key given, and reverses the list, so it is in descending order

    if leaderboard:
        displayData(dataSource, sortedList, True)
    else:
        displayData(dataSource, sortedList)


def displayFound(dataSource):  # prints all results that match a given string
    data = readFile(dataSource)
    textToFind = input("Enter the text to find: ")
    for student in data:
        studentOut = ""
        for item in student:
            studentOut = studentOut + str(item) + ","
        if textToFind in studentOut:
            tFoundText = "\033[0;31m" + textToFind + "\033[0m"  # set text that matches the search to red for visibility
            studentOut = studentOut.replace(textToFind, tFoundText)
            print(studentOut)


def displayFoundField(dataSource):  # prints all results that match a given string, within a given field
    data = readFile(dataSource)
    fieldKeys()
    fieldToSearch = input("Enter the field number to search: ")
    fieldToSearch = int(fieldToSearch)
    textToFind = input("Enter the text to find: ")
    for student in data:
        studentOut = ""
        if textToFind in student[fieldToSearch - 1]:
            for item in student:
                studentOut = studentOut + str(item) + ","
            print(studentOut)


def getStudentID(dataSource):
    studentID = input("Enter Student ID in format 'S000': ")

    length = True
    firstChar = True
    threeNum = True

    taken = False

    try:
        if len(studentID) != 4:
            length = False
        if studentID[0] != "S":
            firstChar = False
        if not int(studentID[1]) > 0 and int(studentID[1]) < 10:  # if the character is not between 1 and 9
            threeNum = False
        if not int(studentID[2]) >= 0 and int(studentID[2]) < 10:  # if the character is not between 0 and 9
            threeNum = False
        if not int(studentID[3]) >= 0 and int(studentID[3]) < 10:  # if the character is not between 0 and 9
            threeNum = False
    except ValueError:  # if a non-numeric character is entered
        threeNum = False

    data = readFile(dataSource)
    for student in data:
        if student[0] == studentID:
            taken = True  # check each student to see if it is already taken

    if taken:
        print("Student ID already taken.")
        return "S000"  # if the student ID is already taken, return a false ID to rerun the function

    if length and firstChar and threeNum and not taken:
        return studentID  # if there are no errors, return the student ID

    # Continue if there are errors

    table = Table(title="Errors Detected")  # create a table to display errors

    table.add_column("Number", justify="right")
    table.add_column("Description")
    errorNum = 1

    if not length:
        table.add_row(str(errorNum), "Length of the Student ID must be 4 digits, including the 'S' character.")
        errorNum += 1
    if not firstChar:
        table.add_row(str(errorNum), "First character of the Student ID must be 'S'.")
    if not threeNum:
        table.add_row(str(errorNum), "The second to fourth characters of the Student ID must be"
                                     " numbers between 0 and 9, beginning at 100.")
    Console().print(table)
    return "S000"  # return a false ID to rerun the function


def createStudent(dataSource):
    data = readFile(dataSource)

    studentID = "S000"
    firstName = "X"
    surname = "X"

    if len(data) < 13:
        while studentID == "S000":
            studentID = getStudentID(dataSource)
        firstName = input("Enter First Name: ")
        surname = input("Enter Surname: ")
        data.append([studentID, firstName, surname, '-', '-', '-', ])
        writeFile(dataSource, data)
        print("Student has been added.")
    else:
        print("Maximum number of students reached. Please delete a record before creating a new one.")


def readData(dataSource):
    data = readFile(dataSource)
    studentNum = input("Enter the Record Number: ")
    studentNum = int(studentNum)
    studentOut = ""
    for item in data[studentNum]:
        studentOut = studentOut + item + ","
    print(studentOut)


def updateStudent(dataSource):
    data = readFile(dataSource)

    try:
        idSearch = input("Enter the Student's ID: ")
        num = 0
        idField = data[0][0]
        while idSearch != idField:
            num += 1
            idField = data[num][0]

        print(data[num])
        score1 = int(input("Update Score 1: "))
        score2 = int(input("Update Score 2: "))
        score3 = int(input("Update Score 3: "))

        data[num][3] = score1
        data[num][4] = score2
        data[num][5] = score3
        print(data[num])

        writeFile(dataSource, data)
        getAverage(dataSource)
        print("Student's data has been updated.")
    except ValueError:
        print("Invalid ID, see all records for list of IDs")
    except IndexError:
        print("Invalid ID, see all records for list of IDs")


def deleteStudent(dataSource):
    data = readFile(dataSource)

    try:
        idSearch = input("Enter the Student's ID: ")

        num = 0
        idField = data[0][0]
        while idSearch != idField:
            num += 1
            idField = data[num][0]
        if num != 0:
            print(data[num])
            data.remove(data[num])

            writeFile(dataSource, data)
            print("Student data has been deleted.")
    except ValueError:
        print("Invalid ID, see all records for list of IDs")
    except IndexError:
        print("Invalid ID, see all records for list of IDs")


def showMenu():
    table = Table()

    table.add_column("Input", justify="right", style="cyan")
    table.add_column("Page Description", style="magenta")

    table.add_row("1", "Display All Records")
    table.add_row("2", "Display Sorted Records")
    table.add_row("3", "Display Found Records")
    table.add_row("4", "Display Found Records by Field")
    table.add_row("5", "Create a Record")
    table.add_row("6", "Read a Record")
    table.add_row("7", "Update a Record")
    table.add_row("8", "Delete a Record")
    table.add_row("9", "Show Leaderboard")

    console = Console()
    console.print(table)


def getSelection():
    showMenu()
    try:
        innerSelection = int(input("Enter your choice: "))
        if innerSelection < 1 or innerSelection > 9:
            raise ValueError
    except ValueError:
        print("Please enter an integer from 1-9.")
        return "failed"
    return innerSelection


# MAIN PROGRAM

fileSource = "studentData.txt"

while True:
    selection = "failed"

    while selection == "failed":
        selection = getSelection()

    match selection:
        case 1:
            displayData(fileSource)
        case 2:
            displaySorted(fileSource)
        case 3:
            displayFound(fileSource)
        case 4:
            displayFoundField(fileSource)
        case 5:
            createStudent(fileSource)
        case 6:
            readData(fileSource)
        case 7:
            updateStudent(fileSource)
        case 8:
            deleteStudent(fileSource)
        case 9:
            displaySorted(fileSource, True)

    pause = input("\nPress enter to continue: ")
