import math

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


file = open("hellbounds_spawns.txt")
data = file.read()

# Split the input into lines
lines = data.split('\n')

# Initialize a 2D array to store the x and z values
processed_data = []

# Parse each line and extract values
for line in lines:
    parts = line.split(':')
    if (parts[0][2:]) == '':  # ignore lines that are empty string
        continue
    index = int(parts[0][2:])
    values = [float(coord.strip()) for coord in parts[1].split(',')[:3]]  # Extract x,y,z values
    processed_data.append([index] + values)


# remove repeat island spawns
i_to_pop = []
for i in range(len(processed_data)):
    for j in range(i + 1, len(processed_data)):
        dist = distance_2d(processed_data[i][1], processed_data[i][3], processed_data[j][1], processed_data[j][3])
        if dist < 40.0:
            print("too close: ", processed_data[i], "and", processed_data[j], "separated by", dist)
            i_to_pop.append(j + 1)


good_points = []  # points that don't conflict with others
for point in processed_data:
    if not point[0] in i_to_pop:
        good_points.append(point)


# patch index numbers
for i in range( len(good_points) - 1 ):
    if good_points[i+1][0] != (good_points[i][0] + 1):
        good_points[i+1][0] = good_points[i][0] + 1


output = ""
for line in good_points:
    output += "- " + str(line[0]) + ":" + str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + ",0,0\n"

print(output)
