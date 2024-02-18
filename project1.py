import random

def roll():

    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter no. of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4")
    else:
        print("Invalid")

max_Score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores)< max_Score:

    for player_idc in range(players):
        print ("\n Player", player_idc +1, "turn has just started\n")
        print("Your total score is:" ,players_scores[player_idc], "\n")
        current_Score = 0
        while True:
            should_roll = input("would you like to roll(y)?")
            if should_roll.lower() != "y":
                break

            value=roll()
            if value == 1:
                print("You scored a 1, Turn Done!")
                current_Score = 0
                break
            else:
                current_Score += value
                print("You rolled a:", value)

            print("YOUR SCORE IS:", current_Score)

        players_scores[player_idc] += current_Score
        print("Your total score is:" , players_scores[player_idc])

for player_idc, score in enumerate(players_scores, 1):
    if players_scores[player_idc] >= max_Score:
        print("Player number", player_idc + 1, "is the winner with a score of:", players_scores[player_idc])
        break

# print(players) 

# value = roll()
# print
# print(value)
 