"""
16-1. San Francisco: Are temperatures in San Francisco more like temperatures
in Sitka or temperatures in Death Valley? Generate a high-low temperature
plot for San Francisco and make a comparison. (You can download weather
data for almost any location from http://www.wunderground.com/history/.
Enter a location and date range, scroll to the bottom of the page, and find a
link labeled Comma-Delimited File. Right-click this link, and save the data as a
CSV file.)
"""
from datetime import datetime
import csv
import matplotlib.pyplot as plt

filename = 'export.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        highs.append(float(row[3]))
        lows.append(float(row[2]))
        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))

# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Format plot
plt.title('Daily highs and lows in Tº, Jan24-Jan25', fontsize=12)

plt.show()