from itu.algs4.sorting.insertion_sort import sort
import operator

# I used Pythons own sort function, since the translated
# version from algs4 library does not have a function, that can access
# the wanted item in the tuples

n = int(input()) # caster input til en integer
listOfStudentTuples = []

gradeDict = {'A+' : 1, 'A' : 2, 'A-' : 3, 'B+' : 4, 'B' : 5, 'B-' : 6, 'C+' : 7, 'C' : 8, 'C-' : 9, 'D+' : 10, 'D' : 11, 'D-' : 12, 'E+' : 13, 'E' : 14, 'E-' : 15, 'FX+' : 16, 'FX' : 17, 'FX-' : 18, 'F+' : 19, 'F' : 20, 'F-' : 21}

while n > 0: 
    studentTuple = (input().split()) # split input into a list of [student, grade]
    studentTuple[1] = gradeDict[studentTuple[1]] # convert grade to gradevalue
    listOfStudentTuples.append(studentTuple[0])
    n -= 1

listOfStudentTuples.sort(key=operator.itemgetter(0)) # sort by name
listOfStudentTuples.sort(key=operator.itemgetter(1)) # sort by gradevalue

for studentTuple in listOfStudentTuples:
    print(studentTuple[0])
