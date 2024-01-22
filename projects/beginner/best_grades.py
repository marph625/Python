"""
The variables list_students and list_grades having been
previously defined and being of the same length, the
function best_grades returns the maximum grade that has been
attributed, the number of students having obtained this
grade and the list of names of these students.

Lists:

list_students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
list_grades = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

Output:

best_grades()
(80, 3, ['c', 'f', 'h'])
"""

list_students = ['Randy', 'Holly', 'Ella', 'Robin', 'Bob', 'Donna', 'Richie', 'Link', 'Zelda', 'Susan']
list_grades = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]


def best_grades():
    grade_max = 0
    nb_students_grade_max = 0
    list_max = []

    for counter in range(len(list_grades)):
        if list_grades[counter] == grade_max:
            nb_students_grade_max += 1
            list_max.append(list_students[counter])
        if list_grades[counter] > grade_max:
            grade_max = list_grades[counter]
            nb_students_grade_max = 1
            list_max = [list_students[counter]]
    return grade_max, nb_students_grade_max, list_max


print(best_grades())
