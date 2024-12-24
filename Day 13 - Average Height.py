heights = [180, 172, 175, 169, 173, 167, 174]
heights_num = len(heights)
students_num = 0
total_height = 0

for height in heights:
    students_num += 1
    total_height += height

avg_height = total_height/heights_num
print("Average Height:", round(avg_height))
print("Total Height:", total_height)
print("Total Number of Heights:", heights_num)

