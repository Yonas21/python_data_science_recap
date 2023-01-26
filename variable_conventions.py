"""
    variables can only starts with letters or underscore
    @ cannot start with number
    @ it's case sensitive
    @ start with alphanumberics(a-z, 0-9, _)
    """

studentname = "Yonas"
student_name = "Yonas"  # snake_case
_student_name = "Yonas"
studentName = "Yonas"  # camelCase
STUDENTNAME = "Yonas"
StudentName = "Yonas"  # PascalCase
student_name_2 = "Yonas"

# print them all
print(studentname)
print(student_name)
print(_student_name)
print(studentName)
print(STUDENTNAME)
print(StudentName)
print(student_name_2)
