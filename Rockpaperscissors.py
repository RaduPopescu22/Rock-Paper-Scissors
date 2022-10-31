import random
class RockPaperScissors:
    def __init__(self):
        None
        
    def move_art(self,move):    
        if move in ("rock",1):
            return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
        elif move in ("paper",2):
            return """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
        else:
            return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    def comp_move(self):
        comp_move = random.randint(1,3)
        return comp_move     
    def player_move(self):
        player_move = input("What is your move (rock, paper, scissors)?\n".lower())
        while player_move not in ("rock", "paper", "scissors"):
            player_move = input("What is your move (rock, paper, scissors)?\n".lower())
        return player_move
    def win(self):
        if p_move == "rock" and c_move == 3 or p_move == "scissors" and c_move == 2 or p_move == "paper" and c_move == 1:
            return True
        else:
            return False
    def tie(self):
        if p_move == "rock" and c_move == 1 or p_move == "paper" and c_move == 2 or p_move == "scissors" and c_move == 3:
            return True
        else:
            return False

rockpaperscissors = RockPaperScissors()
game_state = True
games_count = 0
win_count = 0
tie_count = 0

while game_state:
    p_move = rockpaperscissors.player_move()
    c_move = rockpaperscissors.comp_move()
    print("Your move:\n", rockpaperscissors.move_art(p_move))
    print("Computer move:\n", rockpaperscissors.move_art(c_move))
    if rockpaperscissors.win():
        print("\nYou won!!")
        win_count += 1
    elif rockpaperscissors.tie():
        print("\nIt's a tie!")
        tie_count += 1
    else:
        print("\nYou lost!! :(")
    games_count += 1
    response = input("Press 'q' to quit or press any other key to continue playing!\n")
    if response.lower() == "q":
        game_state = False
    
print(f"You have played {games_count} games with {win_count} win(s) and {tie_count} tie(s)!")














