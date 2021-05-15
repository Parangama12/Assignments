import math
import os
import random
import re
import sys

def gradingStudents(grades):
    modified_grades=[]
    for each in grades:
        if(each<38):
            modified_grades.append(each)
        else:
            if((5-each%5)<3):
                modified_grades.append(each+(5-each%5))
            else:
                modified_grades.append(each)
    return modified_grades                    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()