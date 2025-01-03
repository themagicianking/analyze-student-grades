# read csv file with columns for name, math grade, science grade, and english grade
import csv

names = []
math = []
science = []
english = []

with open('grades.csv') as csv_file:
  grade_reader = csv.reader(csv_file)
  i = 0
  for row in grade_reader:
    if i > 0:
      names.append(row[0])
      math.append(row[1])
      science.append(row[2])
      english.append(row[3])
    i += 1
  
print(names, math, science, english)

# calculate average grade for each subject across all students

# find the student(s) with highest overall grade
# find average grade of each student
# order students from highest to lowest grade
# return highest graded student

# find subject with highest grade

# return all results in readable format