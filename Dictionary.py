#Dictionary is record/array associative
person = dict(Name="choirul ihwan",Age=30,Salary=15000)
print(person)
print(person['Name'])
person['Name'] = "Daffa Abid Aqila"
print(person)
person['Gender'] = "Man"
print(person)

print("delete age")
del(person["Age"])
print(person)