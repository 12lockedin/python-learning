"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""

nums = list(range(1,10))

for num in nums:
    if num == 2:
        print(str(num) + 'nd\n')
    elif num == 3:
        print(str(num) + 'rd\n')
    elif num == 1:
        print(str(num) + 'st\n')
    else:
        print(str(num) + 'th\n')
