import sys

player_active = True
loop_counter = 1

def winner_announcer(loop_counter):
    if loop_counter % 2 == 0:
        print("Player 1 wins!!!") #Cant use return because of sys.exit

        sys.exit(0)
    else:
        print("Player 2 wins!!!") #Cant use return because of sys.exit
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
    if player_input == fizzbuzz_compiler(loop_counter): # if 1 = 1(1) ??? ## Issue is that the p1_input is still a STR instead of being an INT.
        loop_counter += 1
        return loop_counter  # had to change it from return to if
    else:
        return False

while loop_counter < 6:  # Main game loop
    if player_active == True:
        try:
            p1_input = input("Enter your number player 1: ")
            if p1_input == str(p1_input):
                p1_input = int(p1_input)
        except ValueError:
            winner_announcer(loop_counter)
            # If player input is not equal to this it should break and call the winner
            continue
        if input_check(p1_input, loop_counter) == False: # This can be improved (According to PyCharm)
            winner_announcer(loop_counter)
            # Run end game function and declare winner
        else:
            loop_counter += 1
        # continue loop and pass to player 2
        if loop_counter >= 6:
            player_active = False
            break
        try:
            p2_input = input("Enter your number player 2: ")
            if p2_input == str(p2_input):
                p2_input = int(p2_input)
        except ValueError:
            continue
        if input_check(p2_input, loop_counter) == False:
            winner_announcer(loop_counter)
        else:
            loop_counter += 1
    player_active = True