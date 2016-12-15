'''
Name: Harry Brown III
Program: Student Database (File Modifications)
Date: 6/10/16
'''

def displayData():
    #print text file contents
    print('Student Database:' + '\n')
    file = open('students.txt', 'r')
    line = file.read()
    print(line)
    file.close()

def deleteStudent(strName):
    #read from file and remove user input name
    file = open('students.txt', 'r')

    line = file.readline()
    fData = ''
    while line != '':
        if(line == strName + '\n'):
            line = file.readline() #read next line to not add student
        else:
            fData += line #add lines of other students
        line = file.readline()

    cut = fData.rsplit()
    count = len(cut)
    file.close()

    return cut, count

def modifyFile(cut, count):
    #write to file and format
    file = open('students.txt', 'w')
    x = 0
    while x < count:
        line = cut[x] + ' '  + cut[x+1] + '\n' + cut[x+2]
        x = x+3
        file.write(line + '\n')
    print('Database updated. Check the file!')
    file.close()

def main():

    #call displayData procedure
    displayData()

    #enter name to delete
    strName = input('Enter the full name of the student to delete: ')

    #call deleteStudent function
    cut, count = deleteStudent(strName)

    #call modifyFile function
    modifyFile(cut, count)

#call main
main()


