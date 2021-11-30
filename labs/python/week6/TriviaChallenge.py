import sys

def open_file(filename, mode='r'):
    try:
        the_file = open(filename, mode)
    except IOError as e:
        print(e)
        print ("Could not open file \nEnding Program.")
        sys.exit()
    
    return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/','\n')
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def get_highscores(f):
    # USERNAME-SCORE
    highscores = {}
    lines = f.readlines()
    for line in lines:
        if line:
            un, score = line.split('-')
            highscores[un] = score
    return highscores

def write_new_highscore(f):
    


def welcome():
    print('''
        WELCOME TO THE TRIVIA GAME
    ''')

def main():
    f = open_file('/Users/samuelwash/Documents/dev/labs/python/week6/trivia.txt', 'r')
    highscoreFile = open_file('dev/labs/python/week6/trivia-highscores.txt', 'r+')
    highscores = get_highscores(highscoreFile)
    get_highscores(highscoreFile)
    breakpoint
    welcome()
    username = input('Enter your username: ')
    score = 0
    while category:
        category, question, answers, correct, explanation = next_block(f)
        print(category)
        print(question)
        for i in range(4):
            print(f'\t {i+1} - {answers[i]}')
        answer = input('>>> ')
        if answer == correct:
            print('Nice one thats right!')
            score += 1
        else: 
            print('Unlucky, thats wrong')

        print(explanation)
        print(f'Score: {score}')
    
    f.close()
    print('---END---')
    print(f'Your score was {score}') 


if __name__ == '__main__':
    main()       