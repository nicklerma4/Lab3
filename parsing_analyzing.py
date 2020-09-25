import retrieve_file
from datetime import datetime, date, time, timedelta
import re
import os

# Opens file to be analyzed
open_file = open("local_copy.log")

# Create counters
total_requests = 0
month_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
day_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
file_count = {"index.html":0}

# Define month file names
monthfile = {1:"January.txt", 2:"February.txt", 3:"March.txt", 4:"April.txt", 5:"May.txt", 6:"June.txt", 7:"July.txt", 8:"August.txt", 9:"September.txt",10:"October.txt", 11:"November.txt", 12:"December.txt"}


# Reads the file line by line and adds to the total_requests counter
for line in open_file:
    total_requests += 1
        
    # Split lines into necessary elements
    line_elements = re.split("([0-9]{2}/[A-Za-z]{3}/[0-9]{4}):([0-9]{2}:[0-9]{2}:[0-9]{2}).*\"([A-Z]+) (.+?) ([HTTP].+)\" ([0-9]{3})", line)
    
    # Check if regex worked for each line
    if len(line_elements) >= 7:
        
        # Add to the day and month counters
        date = datetime.strptime(line_elements[1], "%d/%b/%Y")
        day_count[date.isoweekday()] += 1
        month_count[date.month] += 1
        
        # Checks for specific month file, if one has been created add line to file otherwise create the file and write the line to the file
        if not os.path.exists(monthfile[date.month]):
            file = open(monthfile[date.month], "w")
            file.write(line)
            file.close()
        else:
            file = open(monthfile[date.month], "a")
            file.write(line)
            file.close()

# Determine most requested file
most_requested = "index.html"
most_count = file_count["index.html"]
for filer, count in file_count.items():
    if count > most_count:
        most_requested = filer
        most_count = file_count[filer]
        
# Determine least requested file
least_requested = "index.html"
least_count = file_count["index.html"]
for filer, count in file_count.items():
    if count < least_count:
        least_requested = filer
        least_count = file_count[filer]
            
print("There were", total_requests, "total requests in the time period represented in the log.")

for d in day_count:
    print("There were", day_count[d]," requests during weekday ", d, " during the time period represented in the log.")
        
for m in month_count:
    print("There were", month_count[m]," requests during month ", m, " during the time period represented in th log.")

print("The most requested file was", most_requested, "with a total of", most_count, "requests.")

print("The least requested file was", least_requested, "with a total of", least_count, "requests.")
            
 open_file.close()
            
