cars = ["Maruti","Tata","Hundai","KIA","BYD"]

print(cars)

## modify list

cars[2] = "Volswagon"

print(cars)

## Adding

cars.append("Hyundai")

print(cars)

## Insert at a location

cars.insert(3, "Honda")
print(cars)

## Delete at a index

del cars[2]

print(cars)

## Pop element - deletes the last element in the list

print(cars)
last_element = cars.pop()
print(cars)
print(f" The element in the last was {last_element}")

## Pop a element at a index

print(cars)
next_element = cars.pop(4)
print(f"The next element to go out {next_element} ")

# Sort a list

print("before sorting {}".format(cars))
cars.sort()
print(f"After sorting {cars}")
cars.sort(reverse=True)
print(f" Sorted in desc order {cars}")

# Temp sort of list
cars = ["Maruti","Tata","Hundai","KIA","BYD"]

print("Before temp sort {}".format(cars))

print(f" The temporary sorted list {sorted(cars)}")

print(f"The original list {cars}")

# Reverse the list
cars.reverse()
print(f"The list in reverse order {cars}")

# print the len of list

l = len(cars)

print(f" Length of the list {l}")






