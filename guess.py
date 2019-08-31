import stringDatabase
import game

class guess:

    """
    Game begins from the guess. Guess includes game menu and receives input from the user.
    It is the main class to call other classes.
    """

    def game_begin(self):

        """
        Function game_begin is the main function which enables the game, store inputs from user,
        give feedback for each input from the user.

        """
        option = " "
        print("** The great guessing game **")
        counter_w = 0
        while option != "q":
            word_ch = stringDatabase.stringDatabase(stringDatabase.new_list).word_chosen
            word_ch = word_ch.lower()
            letters = []
            letters_used = []
            letters.clear()
            for l in word_ch:
                letters.append(l)
            incorrect_guess = 0
            gave_up = 0
            letters_trial = 0
            incorrect_letter_try = 0
            counter_w = counter_w + 1
            print("\n\n Word Game "+ str(counter_w) +": Guess the four letter word!")
            c_guess = ["-","-","-","-"]
            guessl = ""
            for w in c_guess:
                guessl = guessl+w
            print("\n\n\n\nCurrent Guess: " + guessl)
            flag = True
            while flag == True:
                menu = "\n\ng = guess, t = tell me, l for a letter, and q to quit, enter your choice: \n"
                option = input(menu).lower()
                if option == "g":
                    guess_entered = input("Enter your four letter guess : \n").lower()
                    if guess_entered != word_ch:
                        incorrect_guess = incorrect_guess + 1
                        if incorrect_guess == 1:
                            print("\n\nFEEDBACK: Incorrect guess! Try again, you can do it!")
                        elif incorrect_guess == 3:
                            print("\n\nFEEDBACK: This guess isn't right! Come on! Try harder!")
                        elif incorrect_guess == 5:
                            print("\n\nFEEDBACK: Wrong guess! Try again, you are not tired yet!")
                        else:
                            print("\n\nFEEDBACK: Bad guess! Try again mate!")
                        guessl = ""
                        for w in c_guess:
                            guessl = guessl + w
                        print("\n\n\n\nCurrent Guess: " + guessl)
                    else:
                        guessl = ""
                        for w in c_guess:
                            guessl = guessl + w
                        print("\n\n\n\nCurrent Guess: " + guessl)
                        gave_up_guess = 0
                        quit_guess = 0
                        game.game().score_Calculator(word_ch, gave_up_guess, letters_trial, incorrect_letter_try,
                                                     incorrect_guess, guessl, quit_guess)
                        print("\n\nFEEDBACK: You got it right, Well played!")
                        print("Word is: " + word_ch)
                        flag = False
                elif option == "t":
                    gave_up_guess = 1
                    quit_guess = 0
                    game.game().score_Calculator(word_ch, gave_up_guess, letters_trial, incorrect_letter_try,
                                                 incorrect_guess, guessl, quit_guess)
                    print("\n\nThe right word is: '" + word_ch+"'.  Now Try again!\n\n")
                    gave_up = gave_up + 1
                    flag = False
                elif option == "l":
                    letter_entered = input("Enter the letter you want to try : \n").lower()
                    if letters_used.count(letter_entered) == 0:
                        if len(letter_entered) == 1:
                            letters_trial = letters_trial + 1  # total no. of letter trials
                            l_found = False
                            count_found = 0
                            c_guess_prev = ""
                            for q in c_guess:
                                c_guess_prev = c_guess_prev + q
                            for let in range(0,len(letters)):
                                if letters[let] == letter_entered:
                                    l_found = True
                                    count_found = count_found + 1
                                    c_guess[let] = letter_entered
                            if l_found == True:
                                letters_used.append(letter_entered)
                                guessl = ""
                                for w in c_guess:
                                    guessl = guessl + w
                                if guessl != word_ch:
                                    if count_found == 1:
                                        print("\n\nFEEDBACK: Great guess! You found 1 letter!")
                                    if count_found > 1:
                                        print("\n\nFEEDBACK: Bravo! You found " + str(count_found) + " letters!")
                                    print("\n\n\n\nCurrent Guess: " + guessl)
                                if guessl == word_ch:
                                    print("\n\nFEEDBACK: Well done! You discovered the entire word!")
                                    print("Word is: " + word_ch)
                                    gave_up_guess = 0
                                    quit_guess = 0
                                    game.game().score_Calculator(word_ch, gave_up_guess, letters_trial, incorrect_letter_try,
                                                                 incorrect_guess, c_guess_prev, quit_guess)
                                    flag = False
                            else:
                                incorrect_letter_try = incorrect_letter_try + 1 #total no. of incorrect trials
                                if incorrect_letter_try == 1:
                                    print("\n\nFEEDBACK: No such letter in this word! Try again, you can do it!")
                                elif incorrect_letter_try == 3:
                                    print("\n\nFEEDBACK: This letter is not in the word! Come on! Try harder!")
                                elif incorrect_letter_try == 5:
                                    print("\n\nFEEDBACK: Bad letter! Try again, you are not tired yet!")
                                else:
                                    print("\n\nFEEDBACK: No letter found! Try again mate!")
                                print("\n\n\n\nCurrent Guess: " + guessl)
                        else:
                            print("\n\nFEEDBACK: Don't try to cheat me! You are supposed to enter one letter only!")
                            print("\n\n\n\nCurrent Guess: " + guessl)
                    else:
                        print("\n\nFEEDBACK: You have already found this letter, Try a different letter!")
                        print("\n\n\n\nCurrent Guess: " + guessl)

                elif option == "q":
                    quit_guess = 1
                    gave_up_guess = 0
                    game.game().score_Calculator(word_ch, gave_up_guess, letters_trial, incorrect_letter_try,
                                                 incorrect_guess, guessl, quit_guess)
                    flag = False
                    print("\n \n Thank you for playing genius!")
                else:
                    print("\n \n Aaah! Not a correct option! Choose again!")


guess().game_begin()

