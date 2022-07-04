import csv

brightstar_1 = []
dwarfstar_2 = []

with open("bright_star.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        brightstar_1.append(row)

with open("dwarf_star_new.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dwarfstar_2.append(row)

headers_1 = brightstar_1[0]
planet_data_1 = brightstar_1[1:]

headers_2 = dwarfstar_2[0]
planet_data_2 = dwarfstar_2[1:]

headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("merged_star.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)