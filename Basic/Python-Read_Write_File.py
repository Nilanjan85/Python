# General File handling in Python

# Reading File in Python entire content

with open('text_file.txt') as file_object:
    content = file_object.read()
    print(content)

# Reading line by line

file_name = 'text_file.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# Reading the lines outside the with loop. with loop is helpful to open and close the cursor automatically

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# working with the file contents

with open(file_name) as file_object:
    lines = file_object.readlines()

a_string = ''

for line in lines:
    a_string += line.rstrip()

print(a_string)
print(len(a_string))

with open('text_file1.txt') as file_object:
    content = file_object.readline()


t_str = ''

for line in content:
    t_str += line

print(t_str.replace('dog', 'cat'))

# write file

with open('text_file2.txt','w') as file_object:
    file_object.write('This is first line')

# writing multiple lines

with open('text_file3.txt','w') as file_object:
    file_object.write('This is first line \n')
    file_object.write('This is second line \n')





