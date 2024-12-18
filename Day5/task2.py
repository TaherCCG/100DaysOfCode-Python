# Highest score from a list of scores

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_scores = sum(student_scores)
print(f"Total exam scores: {total_exam_scores}")


max_score = 0
for score in student_scores:
    max_score += score

print(f"Sum of scores: {max_score}")

average_score = max_score / len(student_scores)
print(f"Average score: {average_score}")

max_score = max(student_scores)
print(f"Highest score: {max_score}")

# check highest score
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Highest score: {max_score}")

lowest_score = max_score
for score in student_scores:
    if score < lowest_score:
        lowest_score = score

print(f"Lowest score: {lowest_score}")
