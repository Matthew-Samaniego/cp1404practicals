
MENU = """(G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit"""

def main():
    display_menu()
    choice = get_user_choice()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            determine_score_result(score)
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        display_menu()
        choice = get_user_choice()
    print("Thank you and goodbye.")


def print_stars(score):
    print("*" * score)

def display_menu():
    print(MENU)

def get_user_choice():
    choice = input(">>> ").upper()
    return choice

def get_score():
    score = int(input("Enter score: "))
    return score

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