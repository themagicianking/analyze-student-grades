# read csv file with columns for name, math grade, science grade, and english grade
import csv

student_data = []
names = []
math_strings = []
science_strings = []
english_strings = []

with open("grades.csv") as csv_file:
    grade_reader = csv.reader(csv_file)
    i = 0
    for row in grade_reader:
        if i > 0:
            student_data.append(row)
            names.append(row[0])
            math_strings.append(row[1])
            science_strings.append(row[2])
            english_strings.append(row[3])
        i += 1

# calculate average grade for each subject across all students


def convert_grades_to_int(string_grades):
    int_grades = []
    for string in string_grades:
        try:
            int_grades.append(int(string))
        except:
            continue
    return int_grades


math_grades = convert_grades_to_int(math_strings)
science_grades = convert_grades_to_int(science_strings)
english_grades = convert_grades_to_int(english_strings)


def find_average_grade(grades):
    length = len(grades)
    if length > 0:
        return sum(grades) / length
    else:
        return "Insufficient data."


def find_average_grades(math, science, english):
    averages = [math, science, english]
    clean_averages = list(
        map(lambda subject: subject if isinstance(subject, float) else 0.0, averages)
    )

    return {
        "math": clean_averages[0],
        "science": clean_averages[1],
        "english": clean_averages[2],
    }


average_math_grade = find_average_grade(math_grades)
average_science_grade = find_average_grade(science_grades)
average_english_grade = find_average_grade(english_grades)

average_grades = find_average_grades(
    average_math_grade, average_science_grade, average_english_grade
)

# find the student(s) with highest overall grade


def find_personal_average(student):
    string_grades = student[1:]
    int_grades = convert_grades_to_int(string_grades)
    return find_average_grade(int_grades)


def find_personal_averages(students):
    personal_averages = list(
        map(lambda student: find_personal_average(student), students)
    )
    return personal_averages


personal_averages = find_personal_averages(student_data)


def find_highest_average_students(students, averages):
    highest_average_students = []
    highest_average = max(averages)
    indices = list(
        filter(lambda i: averages[i] == highest_average, range(len(averages)))
    )
    for index in indices:
        highest_average_students.append(students[index][0])
    return highest_average_students


highest_average_students = find_highest_average_students(
    student_data, personal_averages
)

# find subject with highest grade


def find_highest_averaged_subject(subjects):
    if (subjects["math"] > subjects["science"]) & (
        subjects["math"] > subjects["english"]
    ):
        return "Math"
    elif (subjects["science"] > subjects["math"]) & (
        subjects["science"] > subjects["english"]
    ):
        return "Science"
    else:
        return "English"


highest_averaged_subject = find_highest_averaged_subject(average_grades)


# return all results in readable format


def print_findings(average_grades, highest_average_students, highest_averaged_subject):
    print(
        "The average math grade is {math_grade}%.".format(
            math_grade=average_grades["math"]
        )
    )
    print(
        "The average science grade is {science_grade}%.".format(
            science_grade=average_grades["science"]
        )
    )
    print(
        "The average English grade is {english_grade}%.".format(
            english_grade=average_grades["english"]
        )
    )
    if len(highest_average_students) > 1:
        print("The highest averaging students are:")
        for student in highest_average_students:
            print(student)
    else:
        print(
            "The highest averaging student is {student}.".format(
                highest_average_students[0]
            )
        )
    print(
        "The subject with the highest average is {subject}.".format(
            subject=highest_averaged_subject
        )
    )


print_findings(average_grades, highest_average_students, highest_averaged_subject)
