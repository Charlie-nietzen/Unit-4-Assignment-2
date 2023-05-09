from rich.console import Console
from rich.table import Table

def readFile(dataSource):
    dataSource = open(dataSource, "r")
    dataIn = dataSource.read()
    dataSource.close()
    dataIn = eval(dataIn)
    return dataIn


def writeFile(dataSource, data):
    dataSource = open(dataSource, "w")
    data = str(data)
    dataSource.write(data)
    dataSource.close()


def fieldKeys():
    print("Key for Sorting:\n1: ID\n2: First Name\n3: Last Name\n4: Score 1\n5: Score 2\n6: Score 3")


def displayData(dataSource, data=None):
    dataTable = Table()

    dataTable.add_column("ID"), dataTable.add_column("First Name"), dataTable.add_column("Last Name")
    dataTable.add_column("Score 1"), dataTable.add_column("Score 2"), dataTable.add_column("Score 3")

    if data is None:  # if data is empty, read the data from the file
        data = readFile(dataSource)

    for student in data:
        studentOut = []
        for item in student:
            studentOut.append(item)
        dataTable.add_row(studentOut[0], studentOut[1], studentOut[2], studentOut[3], studentOut[4], studentOut[5])

    console = Console()
    console.print(dataTable)


def displaySorted(dataSource):
    data = readFile(dataSource)
    fieldKeys()
    fieldToSort = input("Sort Records by which Field: ")
    fieldToSort = int(fieldToSort)
    sortedList = sorted(data, key=lambda studentNum: studentNum[fieldToSort - 1])
    displayData(dataSource, sortedList)
    print("Display Sorted Records Complete.")


def displayFound(dataSource):
    data = readFile(dataSource)
    textToFind = input("Enter the text to find: ")
    for student in data:
        studentOut = ""
        for item in student:
            studentOut = studentOut + item + ","
        if textToFind in studentOut:
            tFoundText = "\033[0;31m" + textToFind + "\033[0m"
            studentOut = studentOut.replace(textToFind, tFoundText)
            print(studentOut)
    print("Display Found Records Complete.")


def displayFoundField(dataSource):
    data = readFile(dataSource)
    fieldKeys()
    fieldToSearch = input("Enter the field number to search: ")
    fieldToSearch = int(fieldToSearch)
    textToFind = input("Enter the text to find: ")
    for student in data:
        studentOut = ""
        if textToFind in student[fieldToSearch - 1]:
            for item in student:
                studentOut = studentOut + item + ","
            # end for item 
            print(studentOut)
        # end if foundField
    # end for student
    print("Display Found Records Complete.")


# end displayFoundField

def createStudent(dataSource):
    data = readFile(dataSource)
    t1stFld = input("Enter ID: ")
    t2ndFld = input("Enter First Name: ")
    t3rdFld = input("Enter Second Name: ")
    t4thFld = input("Enter Gender: ")
    data.append([t1stFld, t2ndFld, t3rdFld, t4thFld, '-', '-', '-', ])
    writeFile(dataSource, data)
    print("Create Record Complete.")


# end createStudent

def readData(dataSource):
    data = readFile(dataSource)
    studentNum = input("Enter the Record Number: ")
    studentNum = int(studentNum)
    studentOut = ""
    for item in data[studentNum]:
        studentOut = studentOut + item + ","
    print(studentOut)
    # end for student
    print("Read Record Complete.")


# end readData


def updateStudent(dataSource):
    data = readFile(dataSource)
    idSearch = input("Enter the 1st Field: ")
    num = 0
    idField = data[0][0]
    while idSearch != idField:
        num += 1
        idField = data[num][0]
    # end for student
    print(data[num])
    tG1 = input("Update Grade 1: ")
    tG2 = input("Update Grade 2: ")
    tG3 = input("Update Grade 3: ")
    data[num][3] = tG1
    data[num][4] = tG2
    data[num][5] = tG3
    print(data[num])
    writeFile(dataSource, data)
    print("Update Record Complete.")


# end updateStudent


def deleteStudent(dataSource):
    data = readFile(dataSource)
    idSearch = input("Enter ID: ")
    num = 0
    idField = data[0][0]
    while idSearch != idField:
        num += 1
        idField = data[num][0]
    # end for student
    if num != 0:
        print(data[num])
        data.remove(data[num])
    # end if num
    writeFile(dataSource, data)
    print("Delete Record Complete.")


# MAIN
fileSource = "studentData.txt"


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

    console = Console()
    console.print(table)


while True:
    showMenu()
    selection = int(input("Enter your choice: "))

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

    pause = input("\nPress enter to continue: ")
# end while
# end MAIN
