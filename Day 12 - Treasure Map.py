area_1 = ["1", "2", "3"]
area_2 = ["4", "5", "6"]
area_3 = ["7", "8", "9"]
map = [area_1, area_2, area_3]

print(f" {area_1} \n {area_2} \n {area_3}")

area_1 = [" ", " ", " "]
area_2 = [" ", " ", " "]
area_3 = [" ", " ", " "]
spot = int(input("Choose a spot to hide your treasure: "))
#Area 1
if spot == 1:
    area_1[0] = "X"
elif spot == 2:
    area_1[1] = "X"
elif spot == 3:
    area_1[2] = "X"

#Area 2
elif spot == 4:
    area_2[0] = "X"
elif spot == 5:
    area_2[1] = "X"
elif spot == 6:
    area_2[2] = "X"

#Area 3
elif spot == 7:
    area_3[0] = "X"
elif spot == 8:
    area_3[1] = "X"
elif spot == 9:
    area_3[2] = "X"

print(f" {area_1} \n {area_2} \n {area_3}")

