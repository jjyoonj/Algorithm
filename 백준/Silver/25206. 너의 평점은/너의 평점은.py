grade_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5,
              "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
sum_grade = 0
final_score = 0
for i in range(20):
    subject, grade, score = input().split()
    if score != "P":
        sum_grade += float(grade)
        final_score += float(grade) * grade_dict[score]
        
print(final_score/sum_grade)
        