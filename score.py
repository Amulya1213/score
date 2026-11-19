scores = []

n = int(input("Enter number of scores: "))

for i in range(n):
    score = float(input(f"Enter score {i+1}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
