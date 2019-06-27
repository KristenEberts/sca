import cs50

def main():
    goalNum = cs50.get_int("Number of times your chasers got the quaffle through a hoop: ")
    snitchCaught = cs50.get_int("Did your team's seeker catch the snitch? Enter 1 if true, 0 otherwise: ")
    score = final_score(goalNum, snitchCaught)
    print("Your team's final score is: " + str(score))

# TODO: define final_score()

if __name__ == "__main__":
    main()
