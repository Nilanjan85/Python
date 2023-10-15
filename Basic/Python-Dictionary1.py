## create a disctionary from empty

emp = {}

emp["Name"] = "Ram"
emp["sal"] = 2000

print(emp)

del emp["Name"]
print(emp)

## looping through all key value paris

marks = {"eng": 70, "maths" : 89,"geo": 78,"phy":80,}

for key, value in marks.items():
    print(key)
    print(value)

## Looping thorugh keys

for key in marks.keys():
    print(key)

# Loop thorugh key in sorted manner

for key in sorted(marks.keys()):
    print(key)

# Loop thorugh values

for value in marks.values():
    print(value)

fav_lang = {"ram":"python","shyam":"java","jadu":"go","madhu":"python"}

## need a list without duplicate will use set for it

for value in set(fav_lang.values()):
    print(value)

# Nested dictionary - dictionary within a list

student1 = {"marks":40, "roll": 20}
student2 = {"marks":60, "roll": 12}
student3 = {"marks":80, "roll": 32}

classs = [student1,student2,student3]

print(f"Printing the  lsit of dictionary {classs}")

## A List in a dictionary

classs = {
    "marks" : [40,60,80],
    "roll" : [20,12,32],
}

print(classs)

## loop through the dictionary

for i in classs["marks"]:
    print(i)

fav_lang = {
    "ram": ["python","c","c++","java"],
    "shyam": ["c++","c"],
    "jadu": ["java","python"],
    "madhu": ["c++","go","react"]
}

for name, lang in fav_lang.items():
    print(f" {name} 's favourite language are")

    for language in lang:
        print(f"Language are : {language}")

## Dictionary inside dictionary

users = {
    "ramuser": {"fname": "ram", "lname": "ram", "loc": "kol"},
    "shyamuser": {"fname": "shyam", "lname": "shyam", "loc": "chennai"},
    "jhaduuser": {"fname": "jhadu", "lname": "jhadu", "loc": "del"},
}

for username, user_info in users.items():
    print(f"Details for user {username}")
    full_name = user_info["fname"] + " " + user_info["lname"]
    print(f"Full name : {full_name}")

    print("Location : "+user_info["loc"])




