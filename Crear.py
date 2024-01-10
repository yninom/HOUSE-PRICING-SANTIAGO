import csv
import random

# Define the range for each variable
precio_range = (20000, 1000000)
habitaciones_range = (1, 5)
piso_range = (1, 20)
barrio_range = (1, 50)

# Generate the data
data = []
for _ in range(10000):
    precio = random.randint(*precio_range)
    habitaciones = random.randint(*habitaciones_range)
    piso = random.randint(*piso_range)
    barrio = random.randint(*barrio_range)
    data.append([precio, habitaciones, piso, barrio])

# Write the data to a CSV file
filename = "Casas.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Precio", "Habitaciones", "Piso", "Barrio"])  # Write the header
    writer.writerows(data)  # Write the data rows

print(f"Database created successfully: {filename}")
