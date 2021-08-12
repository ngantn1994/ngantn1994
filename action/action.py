from csv import reader

# dictionary for omiyage data
omiyage = {}

def get_table_line(history_row):
  omiyage_value = int(history_row[0]) % 32
  omiyage_id = str(omiyage_value)
  omiyage_type = omiyage[omiyage_id][1]
  omiyage_name = omiyage[omiyage_id][2]
  return("| @<a href=\"https://github.com/" + history_row[2] + "\">" + history_row[2] + "</a> | " + history_row[1] + " | " + omiyage_name + " <img src=\"https://ntuyetngan.com/public/github/omiyage/" + omiyage_type + "/32/" + omiyage_id +".png\"> |\n")

# read omiyage data and store in omiyage dictionary
with open('./action/omiyage.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        omiyage[row[0]] = row

result = []

# read the first half of the template
with open('./action/top.md', 'r') as f:
  for line in f:
    result.append(line)

gacha_lines = []

# read the gacha history
with open('./action/history.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        gacha_lines.append(get_table_line(row))

for line in reversed(gacha_lines):
    result.append(line)

# read the second half of the template
with open('./action/bottom.md', 'r') as f:
    for line in f:
        result.append(line)

f = open("./README.md", "w")
for row in result:
    f.write(row)
f.close()