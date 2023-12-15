import os

turn_player ="X"
winner = "-"
scores = []
turn_counter = 0
for i in range(0,10):
    scores.append("-")

def main():
    display(scores)
    while(winner == "-"):
        global turn_player

        play = int(input("make your play"))
        if  play < 10 and play >= 1:
            if scores[play] == "-":
                scores[play] = turn_player  
                turn_player = change_player(turn_player)
                display(scores)
                check_winner(scores)
            else:
                error_note()
        else:
            error_note()
def error_note():
    os.system("cls")
    display(scores)
    print("please make a valid play")

def check_winner(scores):
    global winner
    global turn_counter
    for i in range(1,4):
        check_clms(i)
    for i in range(1,8,3):
        check_rows(i)
    if scores[1] == scores[5] and scores[5] == scores[9] and scores[1] != "-":
        winner = scores[1]
    if scores[3] == scores[5] and scores[5] == scores[7] and scores[3] != "-":
        winner = scores[3]
    if winner != "-":
        print(f"the winner is {winner}")
        exit()
    turn_counter += 1
    if turn_counter == 9 and winner == "-":
        print("its a draw")
        exit() 

def check_rows(i):
    global winner
    if scores[i] == scores[i+1] and scores[i+1] == scores [i+2] and scores[i] != "-":
        winner = scores[i]

def check_clms(i):
    global winner
    if scores[i] == scores[i+3] and scores[i+3] == scores[i+6] and scores[i] != "-":
        winner = scores[i]

def change_player(turn_player):
    if turn_player == "X":
        turn_player = "0"
    else:
        turn_player = "X"       
    return turn_player

def display(scores):
    os.system("cls")
    print(
    f""" {turn_player} player`s turn 
    {scores[1]} | {scores[2]} | {scores[3]}  
    {scores[4]} | {scores[5]} | {scores[6]}
    {scores[7]} | {scores[8]} | {scores[9]}
    """)
    
if __name__ == "__main__":
    main()