"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    # score = float(input("Enter your score: "))
    score = random.randint(1, 100)
    determine_score_result(score)
    print(determine_score_result(score))

def determine_score_result(score):
    if score < 0:
        score_result = ("Invalid score")
    elif score >= 90:
        score_result = ("Excellent")
    elif score >= 50:
        score_result = ("Pass")
    else:
        score_result = ("Bad")
    return score_result

main()



