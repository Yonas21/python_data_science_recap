# declare and assign variables
string_version = str(3)
int_version = int(3)
float_version = float(3)

# string can be declared with single or double qoutes
student_name = "Yonas"

sur_name = 'Alem'

full_name = student_name + ' ' + sur_name
# print all of them
print(type(string_version))
print(int_version)
print(float_version)

print("Hi, My name is, my Name is: ", full_name)

# multiple assignment
name, middle_name, last_name = 'Yonas', 'Alem', 'Atalay'
fullName = name + ' ' + middle_name + ' ' + last_name
print("FullName: ", fullName)

# unpack collections
fruits = ['apple', 'banana', 'cherry']
apple, banana, cherry = fruits

print(apple)
print(banana)
print(cherry)
