import random
def play():
    
    user = input("Whats your choice 'r' for rock 'p' for paper and 's'for scissors & 'q'for quit the game: ")
    computer = random.choice(['r','p','s'])
    if user == 'q':
        exit()

    if user == computer:
        return "Its a tie"
    if is_win(user,computer):
        return "You won!"

    return "You lost!"

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p'and opponent == 'r'):
        return True
while(True):
    print(play())