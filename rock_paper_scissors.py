import random


def play():
    user = input("Type (r) for rock, (p) for paper and (s) for scissors\nRock!, Paper!!, Scissors!!!\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a tie!"
    if isWin(user, computer):
        return "You won!"

    return "You lost!"


def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


if __name__ == "__main__":
    print(play())
