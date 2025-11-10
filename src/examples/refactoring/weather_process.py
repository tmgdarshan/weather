"""This script is badly written on purpose to demonstrate refactoring."""

import csv, math

# Constants
Temp_Threshold = 25
Fahrenheit_Offset = 32
Celsius_to_Fahrenheit_Factor = 1.8

# Load weather data
Path = "./../../../data/weather_data.csv"


# Convert temp in Celsius to Fahrenheit above the threshold temp
def convert_temp(a):
    temp_C = []
    for i in a:
        if float(i[1]) > Temp_Threshold:
            temp_C.append(
                float(i[1]) * Celsius_to_Fahrenheit_Factor + Fahrenheit_Offset
            )
        else:
            temp_C.append(float(i[1]))
    return temp_C


def calculate_sum(a):
    s = 0
    for i in a:
        s += i
    return s


# Load the weather data
data_path = open(Path)
data_load = list(csv.reader(data_path))
data_path.close()
weather_data = data_load[1:]
x = []

# Temperature statistics
for i in weather_data:
    x.append([i[0], i[1], i[2], i[3], i[4]])
total_temps = convert_temp(x)
sum_of_temps = calculate_sum(total_temps)
print("sum", sum_of_temps)
print("avg", sum_of_temps / (len(total_temps) if len(total_temps) else 1))

# Wind Statistics
total_wind = 0
for i in weather_data:
    u = float(i[3])
    v = float(i[4])
    total_wind += math.sqrt(u * u + v * v)
print("wind", total_wind / len(data_load))
