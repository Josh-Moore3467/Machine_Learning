
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


