# read csv file with columns for name, math grade, science grade, and english grade
import csv

student_data = []
names = []
math_strings = []
science_strings = []
english_strings = []

with open('grades.csv') as csv_file:
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
    return sum(grades)/length
  else:
    return "Insufficient data."

average_math_grade = find_average_grade(math_grades)
average_science_grade = find_average_grade(science_grades)
average_english_grade = find_average_grade(english_grades)

# find the student(s) with highest overall grade

def find_personal_average(student):
  string_grades = student[1:]
  int_grades = convert_grades_to_int(string_grades)
  return find_average_grade(int_grades)

def find_personal_averages(students):
  personal_averages = map(lambda student: find_personal_average(student), students)
  return list(personal_averages)

personal_averages = find_personal_averages(student_data)

def find_highest_average_students(students, averages):
  highest_average_students = []
  highest_average = max(averages)
  indices = list(filter(lambda i: averages[i] == highest_average, range(len(averages))))
  for index in indices:
    highest_average_students.append(students[index][0])
  return highest_average_students

print(find_highest_average_students(student_data, personal_averages))

# find subject with highest grade

# return all results in readable format