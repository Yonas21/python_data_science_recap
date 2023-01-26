statement = '''
this is Another one
which are willing to do
'''
print(statement)
print(statement[1])  # strings are arrays

# go through an array
# for i in statement:
#     print(i)


# count length of statements
print("length of statement ----> ", len(statement))


# check string if it exists in another one
full_name = 'Yonas Alem Atalay'

if 'Yonas' in full_name:
    print("'Yes', 'Yonas ' is present in: ", full_name)


if 'Yonas21 ' not in full_name:
    print("'Yes', 'Yonas ' is present not in: ", full_name)


# slicing strings

print(full_name[-5:-2])


# modifying strings
print(full_name.upper())  # change strings to uppercase
print(full_name.lower())  # change strings to lowercase
print(full_name.lower())  # remove white space before/after text
