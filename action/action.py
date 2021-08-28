from csv import reader

########### functions to be used ###########

# generate the line from gacha history
def gen_table_line(omiyage, history_row):
    omiyage_value = int(history_row[0]) % 32
    omiyage_id = str(omiyage_value)
    omiyage_type = omiyage[omiyage_id][1]
    omiyage_name = omiyage[omiyage_id][2]
    return("| @<a href=\"https://github.com/" + history_row[2] + "\">" + history_row[2] + "</a> | " + history_row[1] + " | " + omiyage_name + " <img src=\"https://ntuyetngan.com/public/github/omiyage/" + omiyage_type + "/32/" + omiyage_id +".png\"> |\n")

# read omiyage data and store in omiyage dictionary
def get_omiyage_data(file):
    # dictionary for omiyage data
    omiyage = {}
    
    with open(file, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            omiyage[row[0]] = row

    return omiyage

# read a fixed data file
def get_static_lines(file):
    lines = []
    with open(file, 'r') as f:
      for line in f:
        lines.append(line)
    return lines

# get the gacha lines
def get_gacha_lines(file, omiyage, skip_username, limit):
    lines = []
    gacha_lines = []

    # read the gacha history
    with open(file, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            if row[2] == skip_username:
                continue
            gacha_lines.append(gen_table_line(omiyage, row))

    count = 0

    for line in reversed(gacha_lines):
        lines.append(line)
        count += 1
        if count == limit:
            break
    return lines

########### end of functions to be used ###########
########### main function: actual file reading and code generating ###########
omiyage_data_file = './action/omiyage.csv'
template_top_file = './action/top.md'
gacha_history_file = './action/history.csv'
template_bottom_file = './action/bottom.md'
result_file = './README.md'

username = 'ngantn1994'
history_limit = 15

omiyage_data = get_omiyage_data(omiyage_data_file)
result = get_static_lines(template_top_file) + get_gacha_lines(gacha_history_file, omiyage_data, username, history_limit) + get_static_lines(template_bottom_file)
f = open(result_file, "w")
for row in result:
    f.write(row)
f.close()