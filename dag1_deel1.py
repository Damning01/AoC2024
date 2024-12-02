import math
location_id_1 = []
location_id_2 = []
location_distance = []

# open the text file
with open ('dag1_deel1_input.txt', 'rt') as locations:
    for location in locations:
# make 2 lists: 1 of the first column, one of the second column
        location_id_1.append(int(location[:5]))
        location_id_2.append(int(location[-6:13:]))


# sort both lists from smallest location id to largest location id
location_id_1.sort()
location_id_2.sort()


print('Location ID 1', location_id_1)
print('Location ID 2', location_id_2)

# calculate the distance between item 1 of the left list, to item 2 of the right list (so 7 - 3 = 4)
for location_id in range(0, len(location_id_1)):
    location_distance.append(location_id_2[location_id] - location_id_1[location_id])
print("Result:", location_distance)


# add up the total distances of all location id pairs
print("Added up:", sum(location_distance))
