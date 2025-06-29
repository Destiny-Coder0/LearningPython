#Tuple – Immutable lists(You can not change)
#Set – Collections containing unique elements
#Dictionary – Key-value matches

numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#first 3 elements
#for i in range(3):
#print("numbers[i]")

for num in numbers[:3]:
    print(num)


cities = {"New York", "Istanbul", "Tokyo", "Amsterdam", "Rome", "Istanbul"}

cities.add("London")

print(cities)

students={}

students["Name"]= "James"
students["Age"]=20
students["Score"]=80

print(students)