#2 Player game of FizzBuzz
#Big thanks to Shunnez!

import sys

player_active = True
loop_counter = 1

def winner_announcer(loop_counter):
    if loop_counter % 2 == 0:
        print("Player 1 wins!!!")

        sys.exit(0)
    else:
        print("Player 2 wins!!!")
        sys.exit(0)

def fizzbuzz_compiler(step):
    """compiles latest expected result of fizzbuzz"""
    if step % 3 == 0 and step % 5 == 0:
        return "FizzBuzz"
    elif step % 3 == 0:
        return "Fizz"
    elif step % 5 == 0:
        return "Buzz"
    else:
        return step

def input_check(player_input, loop_counter):
    """Takes in player_input and checks it against fizzbuzz compiler"""
    if player_input == fizzbuzz_compiler(loop_counter):
        loop_counter += 1
        return loop_counter
    else:
        return False

while loop_counter < 20:
    if player_active:
        try:
            p1_input = input("Enter your number player 1: ")
            if p1_input == str(p1_input):
                p1_input = int(p1_input)
                if input_check(p1_input, loop_counter) == False:
                    winner_announcer(loop_counter)
        except ValueError:
            if input_check(p1_input, loop_counter) == False:
                winner_announcer(loop_counter)
        loop_counter += 1
        if loop_counter >= 20:
            player_active = False
            break
        try:
            p2_input = input("Enter your number player 2: ")
            if p2_input == str(p2_input):
                p2_input = int(p2_input)
                if input_check(p2_input, loop_counter) == False:
                    winner_announcer(loop_counter)
        except ValueError:
            if input_check(p2_input, loop_counter) == False:
                winner_announcer(loop_counter)
        loop_counter += 1
    player_active = True

#TODO: Refactor the living hell out of this