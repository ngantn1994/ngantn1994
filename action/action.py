from csv import reader

# dictionary for omiyage data
omiyage = {}

def get_table_line(history_row):
  omiyage_value = int(history_row[0]) % 32
  omiyage_id = str(omiyage_value)
  omiyage_type = omiyage[omiyage_id][1]
  omiyage_name = omiyage[omiyage_id][2]
  return("| @" + history_row[2] + " | " + history_row[1] + " | " + omiyage_name + " <img src=\"https://ntuyetngan.com/public/github/omiyage/" + omiyage_type + "/32/" + omiyage_id +".png\"> |\n")

# read omiyage data and store in omiyage dictionary
with open('omiyage.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        omiyage[row[0]] = row

result = []

# read the first half of the template
with open('top.md', 'r') as f:
  for line in f:
    result.append(line)

# read the gacha history
with open('history.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        result.append(get_table_line(row))
        
# read the second half of the template
with open('bottom.md', 'r') as f:
    for line in f:
        result.append(line)

print(result)

f = open("../README.md", "w")
for row in result:
    f.write(row)
f.close()