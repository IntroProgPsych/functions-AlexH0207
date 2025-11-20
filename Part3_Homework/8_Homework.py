# 1.(Mandatory) Write a function called calculate_grade(score)
#    that RETURNS the correct letter grade:
#       90+ -> A
#       80-89 -> B
#       70-79 -> C
#       60-69 -> D
#       below 60 -> F
#
# 2. Write another function called display_report(score, grade)
#    that PRINTS something like:
#       Score: 85
#       Grade: B
#
# 3. In the main part of the program:
#       - ask the user for the score
#       - call calculate_grade(score)
#       - call display_report(score, grade)
#
# Keep input() outside the functions.

# Write your code here:

def calculate_grade(score):
    grade=""
    if score<60: grade="F"
    elif score>=60 and score<70: grade="D"
    elif score>=70 and score<80: grade="C"
    elif score>=80 and score<90: grade="B"
    else: grade="A"
    return grade
def display_report(score, grade):
   print(f"Score: {score}\nGrade: {grade}")
score=int(input("Score: "))
calculate_grade(score)
display_report(score, calculate_grade(score))