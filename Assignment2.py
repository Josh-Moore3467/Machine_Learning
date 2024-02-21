#Q1
#def loop range
for i in range (10):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10 - i))    




#Q2
#Def List
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Loop through list to pull odd indexes
for x in range (len(my_list)):
    if(x % 2 == 0):
        print(my_list[x])




#Q3
x = [23, 'Python', 23.98]
output = []
for i in range(len(x)):
    output.append(type(x[i]))
print(output)





#Q4
def unique_list(sample_list):
    unique_list = []
    for i in sample_list:
        if(i not in unique_list):
            unique_list.append(i)
    return unique_list
sample_list = [1,2,3,3,3,3,4,5]
unique_output = unique_list(sample_list)
print(unique_output)





#Q5
def upper_lower(in_string):
    upper = 0
    lower = 0
    for i in in_string:
        if i.isalpha():
            if i.islower():
                lower += 1
            else:
                upper += 1

    print("Number of Uppercase: " + str(upper))
    print("Number of Lowercase: " + str(lower))

in_string = input ("input string: ")
upper_lower(in_string)                    