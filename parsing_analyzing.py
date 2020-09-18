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
