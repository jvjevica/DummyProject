
listEmployee = [
    ['X001', 'Bob Russel', 26, 'Engineering', '2015'] ,
    ['X002', 'Jay Barker', 24, 'Engineering', '2015'] ,
    ['X003', 'Hana Curtis', 24, 'Engineering', '2015'] ,
    ['X004', 'Bryan Moe', 23, 'Marketing', '2015'],
    ['X005', 'Lorencia', 26, 'Human Res.', '2015'],
    ['X006', 'Kai Rivas', 27,'Res & Dev','2015'],
    ['X007', 'Doubby Monro', 25, 'Res & Dev', '2016'],
    ['X008', 'Gonzales', 22, 'Engineering', '2015']
]


def showEmployeeData():
    print('\n        Employee Database of Eco Build Co., Ltd\n')
    print('Index\t| ID No\t| Name\t\t| Age\t| Department\t| Joining Year')
    for i in range(len(listEmployee)):
        print('{}\t| {}\t| {}\t| {}\t| {}\t| {}\t'.format(i, listEmployee[i][0], listEmployee[i][1], listEmployee[i][2], listEmployee[i][3], listEmployee[i][4]))


def findIndex(x) :
    inputFindIndex = input('Enter {} you are looking for: '.format(x))
    if inputFindIndex == int :
        str(inputFindIndex)
    print('ID No.\t| Name\t\t| Age\t| Department\t| Joining Year')
    for i in range (len(listEmployee)) :
        if inputFindIndex in listEmployee[i] or inputFindIndex.capitalize() in listEmployee[i] or inputFindIndex.lower() in listEmployee[i] or inputFindIndex.upper() in listEmployee[i] :
            print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listEmployee[i][0], listEmployee[i][1], listEmployee[i][2], listEmployee[i][3], listEmployee[i][4]))


def findEmployeeData():
    print('**FIND EMPLOYEE DATA IN DATABASE**')
    print('''
    A. Find employee by ID No.
    B. Find employee by name
    C. Find employee by age
    D. Find employee by department
    E. Find employee by joining year
    ''')
    while True :
        findBy = input('enter menu (A/B/C/D/E): ')
        if findBy == 'a' or findBy == 'A' :
            findIndex('ID No.')
            break
        elif findBy == 'b' or findBy == 'B' :
            findIndex('name')
            break
        elif findBy == 'c' or findBy == 'C' :
            inputFindAge = int(input('Enter age you are looking for: '))
            print('ID No.\t| Name\t\t| Age\t| Department\t| Joining Year')
            for i in range (len(listEmployee)) :
                if inputFindAge in listEmployee[i] :
                    print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listEmployee[i][0], listEmployee[i][1], listEmployee[i][2], listEmployee[i][3], listEmployee[i][4]))
            break
        elif findBy == 'd' or findBy == 'D' :
            findIndex('department')
            break
        elif findBy == 'e' or findBy == 'E' :
            findIndex('joining year')
            break
        else :
            print('please enter the correct menu')
    # nextMenu = input('enter "1" to return to main menu or "0" to close program :')
    # if nextMenu == 1 :


LoopAddNewEmployee = True
def addNewEmployee() :
    global LoopAddNewEmployee
    while LoopAddNewEmployee :
        print('**ADD NEW EMPLOYEE TO DATABASE**')
        print('Enter new employee data below')
        IDNo = input('ID No. : ')
        Name = input('Name : ')
        Age = int(input('Age : '))
        Department = input('Department : ')
        JoiningYear = input('Joining year : ')
        confirmAdd = input('This action cannot be undone. Confirm add data? (Y/ N):')
        if confirmAdd == 'y' or confirmAdd == 'Y' :
            listEmployee.append([IDNo, Name, Age, Department,JoiningYear])
            showEmployeeData()
            print('**New data successfully added**')
            nextMenu = input('enter "Y" to add more data or "0" to return to main menu :')
            if nextMenu == 'Y'or nextMenu == 'y' :
                continue
            elif nextMenu == '0' :
                LoopAddNewEmployee = False
                continue


def updateInput(y,z,menu) :
    while True :
        inputUpdateValue = input('Enter new {} :'.format(menu))
        updateConfirm = input('This action cannot be undone. Confirm update data? (Y/ N) :')
        if updateConfirm == 'y' or updateConfirm == 'Y' :
            listEmployee[y][z] = inputUpdateValue
            print('ID No.\t| Name\t\t| Age\t| Department\t| Joining Year')
            print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listEmployee[y][0], listEmployee[y][1], listEmployee[y][2], listEmployee[y][3], listEmployee[y][4]))
            print('Data succesfuly updated.')
            break
        if updateConfirm == 'n' or updateConfirm == 'N' :
            break

  
def updateEmployeeData():
    print('**UPDATE EMPLOYEE DATA IN DATABASE**')
    showEmployeeData()
    updateIndex = int(input('enter index to be updated : '))
    print('ID No.\t| Name\t\t| Age\t| Department\t| Joining Year')
    print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listEmployee[updateIndex][0], listEmployee[updateIndex][1], listEmployee[updateIndex][2], listEmployee[updateIndex][3], listEmployee[updateIndex][4]))
    while True :
        updateMenu = (input('''
        1 = edit name
        2 = edit age
        3 = edit department
        4 = edit joining year
        0 = cancel

        enter which menu to be updated : '''))
        if updateMenu == '1' :
            updateInput(updateIndex, int(updateMenu), 'name')
            break
        elif updateMenu == '2' :
            updateInput(updateIndex, int(updateMenu), 'age')
            break
        elif updateMenu == '3' :
            updateInput(updateIndex, int(updateMenu), 'department')
            break
        elif updateMenu == '4' :
            updateInput(updateIndex, int(updateMenu), 'joining year')
            break
        elif updateMenu == '0' :
            break
        else :
            print('Please enter the correct menu.')
            continue
    

LoopDeleteNewEmployee = True
def deleteEmployeeData() :
    global LoopDeleteNewEmployee
    print('**DELETE EMPLOYEE DATA IN DATABASE**')
    showEmployeeData()
    while LoopDeleteNewEmployee :
        # deleteIndex = int(input('enter index to be deleted : '))
        deleteIndex = input('enter index to be deleted or "x" to return to main menu: ')
        if deleteIndex == 'x' :
            break
        deleteIndex = int(deleteIndex)
        print('ID No.\t| Name\t\t| Age\t| Department\t| Joining Year')
        print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listEmployee[deleteIndex][0], listEmployee[deleteIndex][1], listEmployee[deleteIndex][2], listEmployee[deleteIndex][3], listEmployee[deleteIndex][4]))
        deleteConfirm = input('This action cannot be undone. Confirm delete above data? (Y/ N) :')
        if deleteConfirm == 'y' or deleteConfirm == 'Y' :
            del listEmployee[deleteIndex]
            print('Data succesfuly removed.')
            showEmployeeData()
        elif deleteConfirm == 'n' or deleteConfirm == 'N' :
            continue
        nextMenu = input('enter "Y" to delete more data or "0" to return to main menu :')
        if nextMenu == 'Y'or nextMenu == 'y' :
            continue
        elif nextMenu == '0' :
            LoopDeleteNewEmployee = False
            continue

LoopMainMenu = True
while LoopMainMenu :
    print('''Welcome to Employee Database of Eco Build Co., Ltd

    How can we help you today?
    1)	Show all employee data
    2)	Find employee data
    3)	Add new employee data
    4)	Update employee data
    5)	Delete employee data
    0)	Exit
    ''')
    inputMenu = input('Enter menu number: ')

    while True :
        if inputMenu == '1' :
            showEmployeeData()
            back = input('Enter "Y" to return to main menu: ')
            if back == 'Y' or back == 'y' :
                break
        elif inputMenu == '2' :
            findEmployeeData()
            back = input('Enter "Y" to return to main menu: ')
            if back == 'Y' or back == 'y' :
                break
        elif inputMenu == '3' :
            addNewEmployee()
            break
        elif inputMenu == '4' :
            updateEmployeeData()
            back = input('Enter "Y" to return to main menu: ')
            if back == 'Y' or back == 'y' :
                break
        elif inputMenu == '5' :
            deleteEmployeeData()
            break
        elif inputMenu == '0' :
            LoopMainMenu = False
            break
        else :
            print('Menu is not available, please enter the correct number.')
            break

print('Thank you for using our service')
    
