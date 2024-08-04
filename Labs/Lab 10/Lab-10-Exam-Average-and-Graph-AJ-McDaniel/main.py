'''
DEVELOPER: AJ McDaniel
COLLABORATOR(S): None
'''
""" This program reads grades from a file, calculates averages, then creates a bar graph.
"""
##### IMPORTS #####
import matplotlib.pyplot as plt
##### CONSTANT VARIABLES #####
INPUT_FILE = 'grades.txt'
##### FUNCTION DEFINITIONS #####
def get_list():
    grades = []
    with open(INPUT_FILE, 'r') as file:
        for line in file:
            grades.append(line.strip().split(','))
    return grades

def average(lst):
    return sum(lst) / len(lst)

def create_student_grade(grades):
    student_final_grades = []
    for student in grades[1:]:  # Ignore the first row
        name = student[0]
        exam_grades = [float(grade) for grade in student[1:]]
        first_three_exams = exam_grades[:3]
        final_exam = exam_grades[3]

        if min(first_three_exams) < final_exam:
            exam_grades[first_three_exams.index(min(first_three_exams))] = final_exam

        final_grade = average(exam_grades)
        student_final_grades.append((name, final_grade))

    return student_final_grades

def plot_graph(tuple_list):
    names, grades = zip(*tuple_list)

    plt.bar(names, grades)
    plt.title("Students Grades")
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.grid(True)
    plt.show()
    
##### MAIN PROGRAM #####
def main():
    grades_list = get_list()
    student_grades = create_student_grade(grades_list)
    plot_graph(student_grades)


main()