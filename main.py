import re
from time import sleep
from line_to_tweet_processing import send_file_line_as_tweets


def pick_line(the_file, what_line):
    for i, line in enumerate(the_file):
        if i == what_line:
            return line


file_order = ['log_data_kirk.txt', 'log_data_picard.txt', 'log_data_personal_picard.txt', 'log_data_janeway.txt']
# Figure out which file we're on and what line select it
location_file = open('log_data/file_location_index.csv', 'r+')
location_file_line = location_file.readline()
log_file_path, line_number = re.split(r'\,+', location_file_line)


# Open file for reading
log_file = open('log_data/' + log_file_path, 'r')
num_lines = sum(1 for line in log_file)
log_file.seek(0)
# Get Line
line = pick_line(log_file, int(line_number))
# Close file
log_file.close()

if line !='\n':
    send_file_line_as_tweets(line)

# Update File
location_file.seek(0)
line_number = int(line_number) + 1
# Check to see if line number is out of bounds of log_file
if line_number >= num_lines:
    next_log_idx = file_order.index(log_file_path) + 1 \
        if file_order.index(log_file_path) + 1 < len(file_order) \
        else 0
    next_log = file_order[next_log_idx]
    line_number = 0
location_file.write(log_file_path + ',' + str(line_number))
location_file.close()
