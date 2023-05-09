from rich.console import Console
from rich.table import Table
from rich import pretty

def displayData(dataSource):
    table = Table()

    table.add_column("ID"),table.add_column("First Name"),table.add_column("Last Name")
    table.add_column("Score 1"), table.add_column("Score 2"), table.add_column("Score 3")

    tData = readFile(dataSource)
    for tRecord in tData:
        tRecordOut = []
        for tField in tRecord:
            tRecordOut.append(tField)
        table.add_row(tRecordOut[0], tRecordOut[1], tRecordOut[2], tRecordOut[3], tRecordOut[4], tRecordOut[5],
                      tRecordOut[6])

    console = Console()
    console.print(table)

def readFile(tFile):
    fileSource = open(tFile, "r")
    tDataIn = fileSource.read()
    fileSource.close()
    tDataIn = eval(tDataIn)
    return (tDataIn)

def writeFile(tFile, tData):
    fileSource = open(tFile, "w")
    tData = str(tData)
    fileSource.write(tData)
    fileSource.close()

def displayData(dataSource):
    tData = readFile(dataSource)
    for tRecord in tData:
        tRecordOut = ""
        for tField in tRecord:
            tRecordOut = tRecordOut + tField + ","
        print(tRecordOut)

def displaySorted(dataSource):
    tData = readFile(dataSource)
    tSortItem = input("Sort Records by which Field: ")
    tSortItem = int(tSortItem)
    tSortedList = sorted(tData, key=lambda tRecordNum: tRecordNum[tSortItem])
    for tRecord in tSortedList:
        tRecordOut = ""
        for tField in tRecord:
            tRecordOut = tRecordOut + tField + ","
        print(tRecordOut)
    print("Display Sorted Records Complete.")

def displayFound(dataSource):
    tData = readFile(dataSource)
    tFindText = input("Enter the text to find: ")
    for tRecord in tData:
        tRecordOut = ""
        for tField in tRecord:
            tRecordOut = tRecordOut + tField + ","
        if tFindText in tRecordOut:
            tFoundText = "\033[0;31m" + tFindText + "\033[0m"
            tRecordOut = tRecordOut.replace(tFindText, tFoundText)
            print(tRecordOut)
    print("Display Found Records Complete.")

def displayFoundField(dataSource):
    tData = readFile(dataSource)
    tFindField = input("Enter the field number to search: ")
    tFindField = int(tFindField)
    tFindText = input("Enter the text to find: ")
    for tRecord in tData:
        tRecordOut = ""
        if tFindText in tRecord[tFindField]:
            for tField in tRecord:
                tRecordOut = tRecordOut + tField + ","
            # end for tField 
            print(tRecordOut)
        # end if tFindText
    # end for tRecord
    print("Display Found Records Complete.")


# end displayFoundField


def createStudent(dataSource):
    tData = readFile(dataSource)
    t1stFld = input("Enter ID: ")
    t2ndFld = input("Enter First Name: ")
    t3rdFld = input("Enter Second Name: ")
    t4thFld = input("Enter Gender: ")
    tData.append([t1stFld, t2ndFld, t3rdFld, t4thFld, '-', '-', '-', ])
    writeFile(dataSource, tData)
    print("Create Record Complete.")


# end createStudent


def readData(dataSource):
    tData = readFile(dataSource)
    tRecordNum = input("Enter the Record Number: ")
    tRecordNum = int(tRecordNum)
    tRecordOut = ""
    for tField in tData[tRecordNum]:
        tRecordOut = tRecordOut + tField + ","
    print(tRecordOut)
    # end for tRecord
    print("Read Record Complete.")


# end readData


def updateStudent(dataSource):
    tData = readFile(dataSource)
    tIDSearch = input("Enter the 1st Field: ")
    tCount = 0
    tIDField = tData[0][0]
    while tIDSearch != tIDField:
        tCount += 1
        tIDField = tData[tCount][0]
    # end for tRecord
    print(tData[tCount])
    tG1 = input("Update Grade 1: ")
    tG2 = input("Update Grade 2: ")
    tG3 = input("Update Grade 3: ")
    tData[tCount][4] = tG1
    tData[tCount][5] = tG2
    tData[tCount][6] = tG3
    print(tData[tCount])
    writeFile(dataSource, tData)
    print("Update Record Complete.")


# end updateStudent


def deleteStudent(dataSource):
    tData = readFile(dataSource)
    tIDSearch = input("Enter ID: ")
    tCount = 0
    tIDField = tData[0][0]
    while tIDSearch != tIDField:
        tCount += 1
        tIDField = tData[tCount][0]
    # end for tRecord
    if tCount != 0:
        print(tData[tCount])
        tData.remove(tData[tCount])
    # end if tCount
    writeFile(dataSource, tData)
    print("Delete Record Complete.")


# MAIN
fileSource = "studentData.txt"

while True:
    displayData(fileSource)
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

    console = Console()
    console.print(table)

    selection = int(input("Enter your choice: "))
    fileSource = "studentData.txt"

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

    print("")
    tPause = input("Press enter to continue: ")
# end while
# end MAIN
