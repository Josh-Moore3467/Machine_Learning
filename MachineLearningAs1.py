import math

#Question1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max = ages[-1]
sumAdv = sum(ages) / len(ages)
rangeOfAges = (max - min)
print(min, max, sumAdv)







#Question2
dog={
    "name":"pickles",
    "color":"brown",
    "breed":"wheener dog",
    "legs":"4",
    "age":"10",
}

student={
    "first_name":"Josh",
    "last_name":"Moore",
    "gender":"Male",
    "age":"25",
    "marital status":"Single",
    "skills":["java,","c++","c#"],
    "country":"USA",
    "city":"Warrensburg",
    "address":"123 Fake Street",
}

print(len(student))
newSkills = ["Rust", "javascript"]

student["skills"].append(newSkills)
print(student["skills"])

keyList = list(student.keys())
valueList = list(student.values())
print(keyList)
print(valueList)







#Question3
sisters = ('Shawna', 'Kim', 'Lori')
brothers = ('Kyle', 'Mike', 'Josh')

siblings = brothers + sisters
print(siblings)

num_sibling = len(siblings)
print(num_sibling)

family_members = siblings + ('Mike', 'Lori')
print(family_members)







#Question4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print("Length of it_companies:", len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(['Blizzard', 'Tesla', 'A2K'])
print(it_companies)

it_companies.remove("Tesla")
print(it_companies)

'''The difference between remove and discard:
remove() throws and error if the element is not present, where discard doesn't
remove removes the specified element from the set, discard will also remove if the element is present
'''
joined_set =  A.union(B)
print(joined_set)

intersection_set = A.intersection(B)
print(intersection_set)

is_subset = A.issubset(B)
print(is_subset)

disjointed = A.isdisjoint(B)
print(disjointed)

A.update(B)
print(A)
B.update(A)
print(B)

symmetric = A.symmetric_difference(B)
print(symmetric)

del it_companies
del A
del B

age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))






#Question5
radius = 30
area_of_circle = math.pi * radius **2
print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

print("Please enter a radius of a circle: ")
user_radius = float(input())
area_of_circle_userin = math.pi * user_radius**2
print(area_of_circle_userin)






#Question6
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
num_unique_words = len(unique_words)
print("Num unique words:" ,num_unique_words)






#Question7
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")








#Question8
radius = 10
#area calc
area = 3.14 * radius **2
#formated output
output = "The area of a circle with radius {} is {} meters square." .format(radius, area)
#print
print(output)






#Question9

"""
#read amount of students
N = int(input("Enter the number of students: "))
#place to store info
weights_lbs = []
weights_kgs = []
#read weight of N students in pounds
print("Enter the weights of", N, "strudents (in pounds): ")
for i in range(N):
    weights_lbs = int(input("Student {} weight (lbs.): ".format(i+1)))
    weights_lbs.append(weights_lbs)
#convert from lbs to kgs
for weight_lbs in weights_lbs:
    weights_kgs = weight_lbs * 0.453592
    weights_kgs.append(weights_kgs)
#print weights
print("\nWeights of students:")
for i in range(N):
    print("Student {}: {} lbs. = {:.2f} kgs.".format(i+1, weight_lbs[i], weights_kgs[i]))  

"""



#Question9
#Read Amount of Students
N = int(input("enter the number of students: "))
#place to store (in lbs)
student_lbs = []
#read in N number of weights
for i in range(N):
    weight = int(input("Enter Weights of students: "))
    student_lbs.append(weight)
 #print lbs list, create list for kgs conversion   
print("Student Weights in LBS:", student_lbs)
student_kgs = []
#convert to kgs and add to kgs list and format.
for i in range(N):
    student_kgs.append(student_lbs[i]/2.205)
formatted = [round(elem,2) for elem in student_kgs]
#print kgs list
print("Student Weight in Kgs: ", formatted)    
