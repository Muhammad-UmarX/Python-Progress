scores = [88, 85, 86, 79, 91, 97, 99, 93, 84]
highest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

print("Highest Score:", highest_score)