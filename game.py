class game:
    """
    Class game is the score calculation class. It contains a dictionary 'freqrecorder' including all the letters
    and their frequency.
    Game records the score, status and more relevant details for each game played by the user.
    """

    freqrecorder = {
        "a": 8.17,
        "b": 1.49,
        "c": 2.78,
        "d": 4.25,
        "e": 12.70,
        "f": 2.23,
        "g": 2.02,
        "h": 6.09,
        "i": 6.97,
        "j": 0.15,
        "k": 0.77,
        "l": 4.03,
        "m": 2.41,
        "n": 6.75,
        "o": 7.51,
        "p": 1.93,
        "q": 0.10,
        "r": 5.99,
        "s": 6.33,
        "t": 9.06,
        "u": 2.76,
        "v": 0.98,
        "w": 2.36,
        "x": 0.15,
        "y": 1.97,
        "z": 0.07,
    }

    score_report = []

    def score_Calculator(self, word, gave_up, letters_trial, letters_incorrect, incorrect_guess, c_guess, quit):

        """
        Function score_Calculator calculates the score of each word played by the user and stores it in a list.
        When user choose option 'q' from menu. It displays the score report for the entire session.

        :param word: It is the correct word to be guessed by the user.
        :param gave_up: If the user choose 't' from the menu then gave_up=1 else gave_up=0.
        :param letters_trial: Total number of letters tried by the user using option 'l' from menu.
        :param letters_incorrect: Total number of incorrect letters guessed by user using option 'l' from menu.
        :param incorrect_guess: Total number of incorrect word guesses by user using option 'g' from menu.
        :param c_guess: The last current guess displayed on the menu before the final word is guessed.
        :param quit: Counter to check if the user has requested quit.

        """
        if gave_up == 1:
            f_list = []
            word_list = []
            c_guess_list = []
            uncovered_score = 0
            for le in word:
                word_list.append(le)
            for w in c_guess:
                c_guess_list.append(w)
            for l in range(0,len(c_guess_list)):
                if c_guess_list[l] == "-":
                    letter = word_list[l]
                    uncovered_score = uncovered_score + game.freqrecorder[letter]
            unc_score = uncovered_score
            score = 0 - uncovered_score
            score = round(score,3)
            f_list = [word, "Gave up", str(incorrect_guess), str(letters_incorrect), score]
            game.score_report.append(f_list)
        elif quit == 1:
            score = 0
            print("\n\n")
            print("{0:4}     {1:4}     {2:7}     {3:11}     {4:14}     {5:7}".format("Game","Word",
                                                                "Status","Bad Guesses","Missed letters","Score"))
            print("{:-^4}     {:-^4}     {:-^7}     {:-^11}     {:-^14}     {:-^7}".format("","","","","",""))
            counter = 0
            fscore = 0
            for i in range(len(game.score_report)):
                counter = counter + 1
                fscore = fscore + game.score_report[i][4]
                print("{0:4}     {1:4}     {2:7}     {3:11}     {4:14}     {5:7}".format(counter,
                    game.score_report[i][0],game.score_report[i][1],game.score_report[i][2],
                    game.score_report[i][3],game.score_report[i][4]))

            fscore = round(fscore,3)
            print("\n Final Score: "+ str(fscore))
        else:
            score = 0
            f_list = []
            word_list = []
            c_guess_list = []
            uncovered_score = 0
            for le in word:
                word_list.append(le)
            for w in c_guess:
                c_guess_list.append(w)
            for l in range(0, len(c_guess_list)):
                if c_guess_list[l] == "-":
                    letter = word_list[l]
                    uncovered_score = uncovered_score + game.freqrecorder[letter]
            unc_score = uncovered_score
            if incorrect_guess != 0:
                score_deducted = incorrect_guess * (unc_score / 10)
                uncovered_score = uncovered_score - score_deducted
            if letters_trial != 0:  # divide by no. of letters trial
                uncovered_score = uncovered_score / letters_trial
            score = uncovered_score
            score = round(score, 3)
            f_list = [word, "Success", str(incorrect_guess), str(letters_incorrect), score]
            game.score_report.append(f_list)



