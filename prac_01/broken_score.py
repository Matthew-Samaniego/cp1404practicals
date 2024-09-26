"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fix this!

score = float(input("Enter your score: "))
if score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Bad")