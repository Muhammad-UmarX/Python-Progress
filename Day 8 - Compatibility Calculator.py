name_1= input("Enter your name: ")
name_2 = input("Enter your partner's name: ")
combined = name_1 + name_2

word_1 = "true"
word_2 = "love"

count_1 = 0
count_2 = 0

for i in word_1:
    if i in name_1:
        count_1 += 1
    if i in name_2:
        count_2 += 1

for j in word_2:
    if j in name_1:
        count_1 += 1
    if j in name_2:
        count_2 += 1

total_count = str(count_1) + str(count_2)
print("Your total score is:", total_count, "out of 100")
