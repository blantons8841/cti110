# Shatika Oliver
# April 26, 2025
# P4HW1
# This Program collects a set number of scores, validates them, drops the lowest score,
# calculates the average of the remaining scores, and determines the letter grade.

# Pseudocode:
# 1. Ask user how many scores they want to enter
# 2. Create a loop to collect that number of scores
# 3. Validate each score to make sure it is between 0 and 100
#    - If invalid, prompt user again until valid
# 4. Store all valid scores in a list
# 5. Find and remove the lowest score from the list
# 6. Calculate the average of the remaining scores
# 7. Determine the letter grade based on the average
# 8. Display:
#    - Lowest score
#    - Modified list (after dropping the lowest score)
#    - Average score
#    - Letter grade

# Step 1: Ask user how many scores
num_scores = int(input("How many scores do you want to enter? "))
print()

# Step 2: Create a list to hold the scores
scores = []

# Step 3: Loop to collect scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
    scores.append(score)

# Step 4: Find and remove the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)

# Step 5: Calculate average
average_score = sum(scores) / len(scores)

# Step 6: Determine letter grade
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Step 7: Display results
print("\n--------------Results-----------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("----------------------------------")

